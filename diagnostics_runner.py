import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
REPORT_PATH = PROJECT_ROOT / "reports" / "diagnostics_report.txt"
TEST_CASE_PATH = PROJECT_ROOT / "test_cases.json"


def execute_operation(operation, input_a, input_b):
    if operation == "ADD":
        return input_a + input_b
    if operation == "SUB":
        return input_a - input_b
    if operation == "AND":
        return input_a & input_b
    if operation == "OR":
        return input_a | input_b
    if operation == "XOR":
        return input_a ^ input_b

    raise ValueError(f"Unsupported operation: {operation}")


def load_test_cases():
    with TEST_CASE_PATH.open("r", encoding="utf-8-sig") as file:
        return json.load(file)


def run_diagnostics(test_cases):
    results = []

    for test_case in test_cases:
        actual = execute_operation(
            test_case["operation"],
            test_case["input_a"],
            test_case["input_b"]
        )

        expected = test_case["expected"]
        passed = actual == expected

        results.append({
            "case_id": test_case["case_id"],
            "operation": test_case["operation"],
            "input_a": test_case["input_a"],
            "input_b": test_case["input_b"],
            "expected": expected,
            "actual": actual,
            "status": "PASS" if passed else "FAIL"
        })

    return results


def build_report(results):
    total_tests = len(results)
    passed_tests = sum(1 for result in results if result["status"] == "PASS")
    failed_tests = total_tests - passed_tests

    lines = [
        "Cloud Compute Diagnostics Report",
        "=" * 40,
        "",
        f"Total Tests: {total_tests}",
        f"Passed: {passed_tests}",
        f"Failed: {failed_tests}",
        "",
        "Diagnostic Results",
        "-" * 40
    ]

    for result in results:
        lines.append(
            f"{result['case_id']} | {result['operation']} | "
            f"Input A: {result['input_a']} | Input B: {result['input_b']} | "
            f"Expected: {result['expected']} | Actual: {result['actual']} | "
            f"{result['status']}"
        )

    lines.extend([
        "",
        "Operational Summary",
        "-" * 40,
        "Compute validation completed using controlled instruction test cases.",
        "Expected outputs were compared against actual execution results.",
        "This simulates a diagnostics workflow used to validate compute reliability before deployment."
    ])

    return "\n".join(lines)


def save_report(report):
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    with REPORT_PATH.open("w", encoding="utf-8") as file:
        file.write(report)


def main():
    test_cases = load_test_cases()
    results = run_diagnostics(test_cases)
    report = build_report(results)

    save_report(report)

    print(report)
    print("")
    print(f"Report saved to: {REPORT_PATH}")


if __name__ == "__main__":
    main()