from csv import writer


def to_json(json_file,users):
    import json
    with json_file:
        json.dump(users, json_file, indent=4)

def to_csv(csv_file,users):
    import csv
    with csv_file:
        
        writer = csv.writer(csv_file)
        
        header = ['name','id','home','shell']
        writer.writerow(header)
        
        rows = [[user['name'],user['id'],user['home'],user['shell']] for user in users]
        writer.writerows(rows)
