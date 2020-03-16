
import argparse
from src import algorithm
from src.file_writer import write_daily_meetings
from src.file_reader import parse_file

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input-file", required=True, help="input file")
    parser.add_argument("-o", "--output-file",
                        required=True, help="output file")
    args = parser.parse_args()

    meetings = parse_file(args.input_file)
    results = algorithm.run(meetings)
    write_daily_meetings(results, args.output_file)
