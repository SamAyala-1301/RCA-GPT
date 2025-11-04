#!/usr/bin/env python3
"""
RCA-GPT Command Line Interface
"""
import argparse
import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

from rca_gpt.parser import LogParser
from rca_gpt.trainer import IncidentClassifier
from rca_gpt.predictor import IncidentPredictor


def cmd_parse(args):
    """Parse logs and save to CSV"""
    parser = LogParser(args.config)
    
    mode = 'append' if args.append else 'overwrite'
    
    output = parser.parse_and_save(
        log_file_path=args.input,
        output_path=args.output,
        mode=mode
    )
    
    print(f"\n✅ Parsing complete: {output}")


def cmd_train(args):
    """Train the ML model"""
    classifier = IncidentClassifier(args.config)
    
    print("🧠 Training incident classifier...")
    print("="*60)
    
    metrics = classifier.train()
    classifier.save_model()
    
    print("\n" + "="*60)
    print("✅ Training complete!")
    print(f"   Accuracy: {metrics['accuracy']:.2%}")
    print(f"   Classes: {', '.join(metrics['classes'])}")


def cmd_predict(args):
    """Predict incident type for a message"""
    predictor = IncidentPredictor(args.config)
    
    if args.message:
        # Single message
        result = predictor.predict(args.message)
        print(f"\nMessage: {result['message']}")
        print(f"Type: {result['incident_type']}")
        print(f"Confidence: {result['confidence']:.2%}")
    
    elif args.batch:
        # Batch from file
        with open(args.batch, 'r') as f:
            messages = [line.strip() for line in f if line.strip()]
        
        results = predictor.predict_batch(messages)
        
        print(f"\n{'Message':<40} {'Type':<20} {'Confidence'}")
        print("="*80)
        for r in results:
            msg = r['message'][:37] + '...' if len(r['message']) > 40 else r['message']
            print(f"{msg:<40} {r['incident_type']:<20} {r['confidence']:>6.1%}")


def cmd_monitor(args):
    """Start monitoring (placeholder for now)"""
    print("🔍 Starting monitor...")
    print("This will be implemented in Sprint 1")
    print("For now, use: bash/log_monitor.sh")


def main():
    parser = argparse.ArgumentParser(
        description='RCA-GPT: AI-powered Root Cause Analysis',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  rca-gpt parse                      # Parse logs to CSV
  rca-gpt train                      # Train ML model
  rca-gpt predict "Invalid token"    # Classify single message
  rca-gpt monitor                    # Start monitoring (coming soon)
        """
    )
    
    parser.add_argument(
        '--config',
        default='config/config.yaml',
        help='Path to config file (default: config/config.yaml)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version='RCA-GPT v1.0.0 (Sprint 0)'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Parse command
    parse_parser = subparsers.add_parser('parse', help='Parse logs to CSV')
    parse_parser.add_argument('-i', '--input', help='Input log file')
    parse_parser.add_argument('-o', '--output', help='Output CSV file')
    parse_parser.add_argument(
        '--append',
        action='store_true',
        help='Append to existing CSV (default: overwrite)'
    )
    
    # Train command
    train_parser = subparsers.add_parser('train', help='Train ML model')
    
    # Predict command
    predict_parser = subparsers.add_parser('predict', help='Predict incident type')
    predict_group = predict_parser.add_mutually_exclusive_group(required=True)
    predict_group.add_argument('message', nargs='?', help='Log message to classify')
    predict_group.add_argument('-b', '--batch', help='File with messages (one per line)')
    
    # Monitor command
    monitor_parser = subparsers.add_parser('monitor', help='Start monitoring')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Route to appropriate function
    commands = {
        'parse': cmd_parse,
        'train': cmd_train,
        'predict': cmd_predict,
        'monitor': cmd_monitor
    }
    
    try:
        commands[args.command](args)
    except Exception as e:
        print(f"\n❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()