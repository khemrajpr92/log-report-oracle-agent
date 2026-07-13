# Parse Access Log and Generate Report

There is an Apache-style access log (`access.log`) in the working directory. Analyze the traffic and generate a JSON report that summarizes what you find.

## Success Criteria

Your solution must:

1. Read the access log file (`/app/access.log`)
2. Count the total number of requests
3. Count the number of unique client IP addresses
4. Identify the most frequently accessed path/URL
5. Write the results to `/app/report.json` in the following JSON format:

```json
{
  "total_requests": <integer>,
  "unique_ips": <integer>,
  "top_path": "<string>"
}
```

## Notes

- The log follows standard Apache Combined Log Format
- The agent must produce valid JSON output
- All three fields (total_requests, unique_ips, top_path) are required
