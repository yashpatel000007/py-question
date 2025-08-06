#!/bin/bash

DATE=$(date +%F)

ps aux > process_log_${DATE}.log

echo "Checking for high memory usage..."
HIGH_MEM=$(ps aux --sort=-%mem | awk 'NR>1 && $4>30')

if [ -n "$HIGH_MEM" ]; then
    echo "⚠️ Warning: Processes using more than 30% memory found!"
    echo "$HIGH_MEM" >> high_mem_processes.log
    echo "$HIGH_MEM"
else
    echo "No high memory usage processes."
fi

ROOT_USAGE=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$ROOT_USAGE" -gt 80 ]; then
    echo "⚠️ Warning: Disk usage on / is above 80% (${ROOT_USAGE}%)"
else
    echo "Disk usage on / is within safe limits (${ROOT_USAGE}%)"
fi

TOTAL_PROCESSES=$(ps aux | wc -l)
HIGH_MEM_COUNT=$(echo "$HIGH_MEM" | wc -l)

echo ""
echo "===== System Health Summary ====="
echo "Total running processes: $TOTAL_PROCESSES"
echo "Processes using >30% memory: $HIGH_MEM_COUNT"
echo "Disk usage on /: ${ROOT_USAGE}%"
echo "================================="
