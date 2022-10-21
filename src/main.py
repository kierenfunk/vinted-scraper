import json
import csv
from os import environ
from vinted import VintedAPI

if __name__ == "__main__":
    '''
    api = VintedAPI(environ.get('SESSION_TOKEN'))
    all_items = []
    result = api.invoices_current()
    all_items += result['invoice_lines']
    for item in result['history']:
        month_result = api.invoice(item['year'], item['month'])
        all_items += month_result['invoice_lines']
        for line in month_result['invoice_lines']:
    json.dump(all_items, open('output.json', 'w'))
    '''

    items = json.load(open('output.json', 'r'))
    with open('output.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([
            'id',
            'date',
            'title',
            'subtitle',
            'amount',
            'currency',
            'type',
            'entity_type',
            'pending'
        ])
        for line in items:
            writer.writerow([
                line['id'] if 'id' in line else None,
                line['date'],
                line['title'],
                line['subtitle'],
                line['amount'],
                line['currency'],
                line['type'],
                line['entity_type'],
                line['pending'] if 'pending' in line else False
            ])