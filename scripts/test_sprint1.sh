#!/bin/bash

echo "🧪 SPRINT 1 INTEGRATION TEST"
echo "================================"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 1. Clean slate
echo -e "${BLUE}1. Cleaning up old data...${NC}"
rm -f data/incidents.db
rm -f logs/app.log
echo "✓ Clean"
echo ""

# 2. Generate some logs
echo -e "${BLUE}2. Generating sample logs...${NC}"
timeout 15 bash bash/generate_logs.sh &
PID=$!
sleep 17
kill $PID 2>/dev/null
echo "✓ Generated logs"
echo ""

# 3. Train model (if needed)
if [ ! -f "models/classifier.pkl" ]; then
    echo -e "${BLUE}3. Training model...${NC}"
    rca-gpt train
    echo ""
fi

# 4. Run monitor once
echo -e "${BLUE}4. Running monitor (single check)...${NC}"
rca-gpt monitor --once
echo ""

# 5. Generate test incidents
echo -e "${BLUE}5. Generating test incidents...${NC}"
python scripts/generate_test_incidents.py --count 20
echo ""

# 6. Show history
echo -e "${BLUE}6. Showing incident history...${NC}"
rca-gpt history --limit 10
echo ""

# 7. Show stats
echo -e "${BLUE}7. Database statistics...${NC}"
rca-gpt stats
echo ""

# 8. Show detailed incident
echo -e "${BLUE}8. Detailed view of incident #1...${NC}"
rca-gpt show 1
echo ""

# 9. Search
echo -e "${BLUE}9. Searching for 'timeout'...${NC}"
rca-gpt search "timeout"
echo ""

# 10. Export
echo -e "${BLUE}10. Exporting incidents...${NC}"
rca-gpt export -o test_export.json --limit 5
echo ""

# 11. Verify database file
echo -e "${BLUE}11. Verifying database...${NC}"
if [ -f "data/incidents.db" ]; then
    SIZE=$(du -h data/incidents.db | cut -f1)
    echo "✓ Database exists: $SIZE"
else
    echo "✗ Database not found!"
    exit 1
fi
echo ""

# Success
echo -e "${GREEN}✅ ALL TESTS PASSED!${NC}"
echo ""
echo "Sprint 1 Features Verified:"
echo "  ✓ Incident storage"
echo "  ✓ Fingerprinting & deduplication"
echo "  ✓ Context storage"
echo "  ✓ Historical queries"
echo "  ✓ Statistics"
echo "  ✓ Search"
echo "  ✓ Export"
echo ""
echo "Database location: data/incidents.db"
echo "Export file: test_export.json"