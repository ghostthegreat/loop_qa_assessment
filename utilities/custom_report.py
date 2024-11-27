from glob import glob


class CustomReporter:
    def __init__(self, allure_results_dir):
        self.allure_results_dir = allure_results_dir
        self.test_results = []

    def on_start(self):
        """Initialize or reset test results if needed."""
        self.test_results = []

    def on_test_end(self, test_name, steps, status, duration):
        """Collect test result data."""
        self.test_results.append({
            'name': test_name,
            'steps': ', '.join(steps),
            'status': status,
            'duration': f"{duration:.2f}s"
        })

    def generate_html_report(self):
        """Generate the custom HTML report based on collected test results."""
        tests_summary = ''.join(
            f"<tr><td>{index + 1}</td><td>{test['name']}</td><td>{test['steps']}</td>"
            f"<td>{test['status'].capitalize()}</td><td>{test['duration']}</td></tr>"
            for index, test in enumerate(self.test_results)
        )

        passed = sum(1 for test in self.test_results if test['status'] == 'passed')
        failed = sum(1 for test in self.test_results if test['status'] == 'failed')
        skipped = sum(1 for test in self.test_results if test['status'] == 'skipped')
        total = passed + failed + skipped

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Test Report</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; background-color: #f9f9f9; }}
                .header-container {{ text-align: center; color: #333; padding: 10px; margin-bottom: 20px; }}
                .chart-container {{ width: 30%; margin: 0 auto; }}
                canvas {{ max-width: 100%; height: auto; }}
                .table-container {{ width: 100%; margin-top: 20px; }}
                table {{ width: 100%; border-collapse: collapse; background-color: #fff; border-radius: 8px; overflow: hidden; }}
                table, th, td {{ border: 1px solid #ddd; padding: 8px; }}
                th {{ background-color: #f2f2f2; text-align: left; }}
                tr:nth-child(even) {{ background-color: #f9f9f9; }}
                tr:hover {{ background-color: #f1f1f1; }}
            </style>
        </head>
        <body>
            <div class="header-container">
                <h1>Test Results Summary</h1>
                <p>Total Tests: {total} | Passed: {passed} | Failed: {failed} | Skipped: {skipped}</p>
                <div class="chart-container">
                    <canvas id="donutChart"></canvas>
                </div>
            </div>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>S.No</th>
                            <th>Test Name</th>
                            <th>Steps</th>
                            <th>Status</th>
                            <th>Time Taken</th>
                        </tr>
                    </thead>
                    <tbody>
                        {tests_summary}
                    </tbody>
                </table>
            </div>
            <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
            <script>
                const ctx = document.getElementById('donutChart').getContext('2d');
                const donutChart = new Chart(ctx, {{
                    type: 'doughnut',
                    data: {{
                        labels: ['Passed', 'Failed', 'Skipped'],
                        datasets: [{{
                            label: 'Test Results',
                            data: [{passed}, {failed}, {skipped}],
                            backgroundColor: ['#4CAF50', '#F44336', '#FFC107'],
                            hoverOffset: 4
                        }}]
                    }},
                    options: {{
                        responsive: true,
                        maintainAspectRatio: false
                    }}
                }});
            </script>
        </body>
        </html>
        """

        with open('test-report.html', 'w') as file:
            file.write(html_content)

    def on_end(self):
        """Finalize report generation."""
        self.generate_html_report()

if __name__ == "__main__":
    reporter = CustomReporter(allure_results_dir='allure-results')
    reporter.on_test_end("Test 1", ["Step 1", "Step 2"], "passed", 1.23)
    reporter.on_test_end("Test 2", ["Step 1", "Step 2"], "failed", 2.34)
    reporter.on_test_end("Test 3", ["Step 1", "Step 2"], "skipped", 0.56)
    reporter.on_end()