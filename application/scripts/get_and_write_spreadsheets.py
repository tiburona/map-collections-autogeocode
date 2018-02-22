import os
from modules import spreadsheet, writer


print('/Users/katie/map_collections_autogeocode/csvs/small_test.csv')
print('/Users/katie/map_collections_autogeocode/keys.txt')
print('Island,City/Town/Hamlet,Stream,River/Creek,Lake/Pond/Reservoir,Island Group,Bay/Harbor,'
      'Department / Province / State,Country,Sea/Gulf/Strait,Ocean')


new_spreadsheet = spreadsheet.Spreadsheet(csv_file='/Users/katie/map-collections-autogeocode/csvs/small_test.csv',
                                      api_file='/Users/katie/map-collections-autogeocode/keys.txt',
                                      location_fields='Island,City/Town/Hamlet,Stream,River/Creek,Lake/Pond/Reservoir,Island Group,Bay/Harbor,'
      'Department / Province / State,Country,Sea/Gulf/Strait,Ocean',
                                          id_field='Tracking Number')


new_spreadsheet.fetch_geocoded_data()

print(new_spreadsheet.location_fields)

dirname, basename = os.path.split(new_spreadsheet.csv_file)
name, ext = os.path.splitext(basename)


new_writer = writer.Writer(new_spreadsheet.records, dirname, name)
new_writer.write_new_location_csv()