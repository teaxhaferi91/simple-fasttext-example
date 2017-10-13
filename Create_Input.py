import json
import argparse

def create_input_fasttext(jsonfile, outfile):
    ''' this function takes as input the json file of review-records and a text file name, and writes the text-reviwes for each record'''

    with open(outfile, 'w') as outf:
        for line in open(jsonfile, 'r'):
            record = json.loads(line)
            outf.write(record['reviewText'] + '\n')
        outf.close()
    return



if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--input', help='json file with review records', default='reviews.json')
    parser.add_argument('--output', help='text file with text-reviews', default='reviews_fasttext.txt')
    args=parser.parse_args()
    create_input_fasttext(jsonfile=args.input, outfile=args.output)
