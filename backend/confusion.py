import matplotlib.pyplot as plt
import numpy as np

data_dictionary = {
    "collaborators":["India Meteorological Department", "imd", "aibp", "Himachal Pradesh Forest Department",
                 "Karnataka Forest Department", "Ludhiana Municipal Corporation", "Punjab Remote Sensing Centre",
                 "Punjab Heritage & Tourism Promotion Board", "national remote sensing center"],
    "viewer" : ["Field Data Viewer","mgnrega","bhuvan-mgnrega"],
"darta":['Archives ','Ordering Satellite Data','Super Site','Remote Sensing Analysis','NRSC data','ISRO data','Open data'],
"dimen":["bhuvan 2d", "isro 2d","2d world map","2d map",],
"house":["Ministry of Housing","Urban Affairs","Housing for All" ,"PMAY"],
'ap':["AP STATE","A.P.STATE HOUSING CORPORATION","state housing corporation"],
"hospi":["Andhra Pradesh Vaidya Seva Trust"," Vaidya Seva Trust","Search hospital" ,"hospital near me"],
"gg":['forum','Bhuvan Discussion Forum','Map the neighborhood in Uttarakhand','MANU',  'Bhuvan Success Stories' ,  'Bhuvan Wish-list'   ,'Developers Section'  , 'Pocket Bhuvan'  , 'Thematic Services' ,  ' NRSC Open EO Data Archive','NOEDA','Bhuvan Usability',"Bhuvan Updates"],
"wb":["Water Spread Meter",'wbis','Water Bodies Information System'],
"disc":["data discovery",'Imagery base maps','Climatology',' meteorology',' atmosphere','Environment','Boundaries','Elevation','Location','Geoscientific information','Inland waters','Oceans','Planning cadastre'],
"threedim":["3D ","map"],
"xx":["Use of Geo-informatics in Rural Road Projects under PMGSY","PMGSY","Rural Road Projects"," Rural Road Projects under PMGSY"],
"watr":["Water Resources Management Support Maharashtra",'wrms',"Water Resources Management Support"],
"aib":["Satellite based AIBP Project Monitoring","About AIBP",'AIBP Phase 2',"AIBP Phase 1","My Layers","AIBP Phase 3 ","Online Monitoring","AIBP Phase 4"],
"nn":["Geo-tagging of Rashtriya Krishi Vikas Yojana ","RKVY","Rashtriya Krishi Vikas Yojana"],
"disaster":["Disaster Services","Disaster","Near Real Time Forest Fire","Forest Fire","Real Time Forest Fire"],
"liv":["Live CDMA Property Tax Data Mapping","Live CDMA","CDMA","Tax Data Mapping"],
"delt":["Deltas of India","Deltas"],
"lol":["Ministry of Agriculture","DARE","Agricultural Research","Education","Animal Husbandry","Dairy","Fisheries","Agriculture and Co-operation","Land Use"],
"mines":["Ministry of Mines","mines",],
"wueee":["Baseline Studies on Water Use Efficiency of Irrigation projects"," WUE"," Water Use Efficiency"],
"road":["Ministry of Road Transport and Highways","Road Transport ","Highways"],
"nuu":["Ludhiana Municipal GIS","GIS"],
"noo":["Tourism Amritsar","Tourism"],
"school":["School Bhuvan","THEMATIC SERIES 1","THEMATIC SERIES 2","Drainage","Natural Vegetation" ,"Wildlife","Physical Features","Population","Census","Admin Boundary","Hydrological Boundary"],
"cetg":["Geospatial Governance",],
"rbi":[" Geo-tagging of Reserve Bank of India", "Reserve Bank of India" ,"RBI" ,"Geo-tagging"],
"store":["Bhuvan Store"],
"cris":["Ministry of Environment,Forest and Climate Change","Centralised Resource Inventory System ","CRIS"],
"coro":["COVID-19","Corona 2020"],
"child":["Ministry of Women & Child Development ","Women Development","Child Development"],
"pm":["MINISTRY OF MINORITY AFFAIRS ","Pradhan Mantri Jan Vikas Karyakram","MINORITY AFFAIRS"],
"obser":["earth observation"],
"saras":["Saraswati Palaeochannels","Saraswati","Palaeochannels"],
"hr":["Bhuvan Haryana"],
'kf':["Karnataka Forest"] ,
"pf":["Punjab Forest"],
"tf":["Telangana Forest"],
"gang":["bhuvan ganga","ganga"],
"hot":["Hot Weather Outlook" ,"Hot Weather" ,"Weather Outlook"],
"FAM":["Farmers Welfare","pmksy","farmer"],
"TOP":["Bhuvan IMD Weather Products","IMD"],
"HP":["Himachal Pradesh Forest"],
'WEB':["WebGIS"],
"NERT":["NCERT","e-learning portal"],
"FLY":["Distribution of Flycatchers","Flycatchers"],
"GOG":["Geographical Indications of India","GI","Geographical Indications"],
"HUM":["Ministry of Human Resource Development","Human Resource Development","Human Resource"]
}
'''test_cases = [
    ("Tell me about water resources", "wb"),
    ("Open DARTA", "https://bhuvan-app3.nrsc.gov.in/data/"),
    # Add more test cases as needed
]

# Initialize counters for True Positives (TP), False Positives (FP), and False Negatives (FN)
tp = fp = fn = 0

# Evaluate the script on test cases
for query, expected_category in test_cases:
    print("User Query:", query)
    
    # Simulate user input
    query = query.lower()  # Convert to lowercase for case-insensitive comparison
    found_category = None
    
    # Check if any category keyword is present in the query
    for category, keywords in data_dictionary.items():
        for keyword in keywords:
            if keyword.lower() in query:
                found_category = category
                break
    
    # Check if the script opened the correct URL or not
    if found_category == expected_category:
        tp += 1  # True Positive
        print("Correct Category!")
    else:
        fp += 1  # False Positive
        print("Incorrect Category. Expected:", expected_category, "Found:", found_category)
    
    # Check for False Negatives
    if found_category is None and expected_category in data_dictionary:
        fn += 1  # False Negative
        print("Expected category not found.")

    print("\n---\n")

# Display the confusion matrix
print("Confusion Matrix:")
print("True Positives (TP):", tp)
print("False Positives (FP):", fp)
print("False Negatives (FN):", fn)'''

# Define a set of test cases with expected results
test_cases = [
    ("Tell me about water resources", "wb"),
    ("Open DARTA", "darta"),
    # Add more test cases as needed
]

# Initialize counters for True Positives (TP), False Positives (FP), and False Negatives (FN)
tp = fp = fn = 0

# Evaluate the script on test cases
for query, expected_category in test_cases:
    # Simulate user input
    query = query.lower()  # Convert to lowercase for case-insensitive comparison
    found_category = None
    
    # Check if any category keyword is present in the query
    for category, keywords in data_dictionary.items():
        for keyword in keywords:
            if keyword.lower() in query:
                found_category = category
                break
    
    # Update confusion matrix counts
    if found_category == expected_category:
        tp += 1  # True Positive
    else:
        fp += 1  # False Positive
        # Check for False Negatives
        if found_category is None and expected_category in data_dictionary:
            fn += 1  # False Negative

# Display the confusion matrix using matplotlib
confusion_matrix = np.array([[tp, fp], [fn, 0]])

fig, ax = plt.subplots()
cax = ax.matshow(confusion_matrix, cmap='Blues')
plt.title('Confusion Matrix')
plt.xticks([0, 1], ['Predicted Correctly', 'Predicted Incorrectly'])
plt.yticks([0, 1], ['Actual Correct', 'Actual Incorrect'])
plt.colorbar(cax)

# Display the counts in each cell
for i in range(2):
    for j in range(2):
        plt.text(j, i, str(confusion_matrix[i, j]), ha='center', va='center', color='black', fontweight='bold')

plt.show()