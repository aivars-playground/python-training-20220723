def create_parser():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', help='export file')
    parser.add_argument('--format', default='json', choices=['json','csv'], type=str.lower)
    return parser

def main():
    import sys
    from clitool import export, users as u
    
    args = create_parser().parse_args()
    users = u.fetch_users()

    if args.path:
        file = open(args.path, 'w', newline='')
    else:
        file = sys.stdout
    
    if args.format == 'json':
        export.to_json(file, users)
    else:
        export.to_csv(file, users)