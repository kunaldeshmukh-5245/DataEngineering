import argparse

parser = argparse.ArgumentParser(description = "Log Extractor")
parser.add_argument("--input", type=str, required=True, help="path to the input log file")
parser.add_argument("--output", type=str, required=True, help="path to the output file")
parser.add_argument("--keywords", type=str, nargs='+', required=True, help="comma-separated keywords to filter logs")

args = parser.parse_args()

print("Input file:", args.input)
print("Output file:", args.output)
print("Keywords:", args.keywords)