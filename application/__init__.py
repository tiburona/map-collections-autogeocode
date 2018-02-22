

from modules.spreadsheet import Spreadsheet

print('/Users/katie/map_collections_autogeocode/csvs/clean_dataset_iz_test.csv')
print('/Users/katie/map_collections_autogeocode/keys.txt')
print('Island,City/Town/Hamlet,Stream,River/Creek,Lake/Pond/Reservoir,Island Group,Bay/Harbor,'
      'Department / Province / State,Country,Sea/Gulf/Strait,Ocean')


spreadsheet = Spreadsheet(csv_file='/Users/katie/map_collections_autogeocode/csvs/clean_dataset_iz_test.csv',
                          api_file='/Users/katie/map_collections_autogeocode/keys.txt',
                          location_fields='Island,City/Town/Hamlet,Stream,River/Creek,Lake/Pond/Reservoir,Island Group,Bay/Harbor,'
      'Department / Province / State,Country,Sea/Gulf/Strait,Ocean')


spreadsheet.fetch_geocoded_data()

print(spreadsheet.location_fields)
