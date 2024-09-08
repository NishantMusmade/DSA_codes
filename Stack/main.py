import sys
from io import StringIO

def find_winning_tokens(tokens, N):
    token_set = set()
    best_pair = None
    smallest_diff = float('inf')
    
    for token in tokens:
        complement = N - token
        if complement in token_set:
            current_diff = abs(token - complement)
            if current_diff < smallest_diff:
                smallest_diff = current_diff
                best_pair = (token, complement)
        token_set.add(token)
    
    if best_pair:
        return sorted(best_pair, reverse=True)
    else:
        return [0]

def main():
    input = sys.stdin.read
    data = input().strip().split('\n')
    
    num_customers = int(data[0].strip())
    tokens = list(map(int, data[1].strip().split()))
    N = int(data[2].strip())
    
    result = find_winning_tokens(tokens, N)
    print(" ".join(map(str, result)))

if _name_ == "_main_":
    # Define test cases
    test_cases = [
        {
            "input": "6\n1 6 3 2 5 4\n7\n",
            "expected": "5 2\n"
        },
        {
            "input": "5\n100 250 120 200 25\n320\n",
            "expected": "200 120\n"
        },
        {
            "input": "4\n10 20 30 40\n50\n",
            "expected": "30 20\n"
        },
        {
            "input": "3\n10 15 20\n30\n",
            "expected": "20 10\n"
        },
        {
            "input": "4\n1 1 1 1\n2\n",
            "expected": "0\n"
        }
    ]

    for i, test_case in enumerate(test_cases):
        sys.stdin = StringIO(test_case["input"])
        expected_output = test_case["expected"]
        
        # Capture the output
        output = StringIO()
        sys.stdout = output
        
        # Run the main function
        main()
        
        # Check the result
        result = output.getvalue()
        assert result == expected_output, f"Test case {i + 1} failed: expected '{expected_output}', got '{result}'"
    
    print("All test cases passed!")

    # Reset stdin and stdout
    sys.stdin = sys._stdin_
    sys.stdout = sys._stdout_