import openai
import requests
import datetime
import pyttsx3
import wikipedia
import webbrowser
import os
import pywhatkit
import speech_recognition as sr
from gtts import gTTS
from tqdm import tqdm
r = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Set your OpenAI API key
openai.api_key = "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"
                        # function which speaks
    
def generate_response(prompt, max_words=100):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.5,
        )
        generated_text = response["choices"][0]["text"]

        # Limit the response to the first 100 words
        words = generated_text.split()[:max_words]
        limited_response = ' '.join(words)

        return limited_response
    except Exception as e:
        # Provide more details about the exception for debugging
        print(f"Error generating response. Exception: {e}")
        return None


# Bhuvan API endpoint
base_url = "https://bhuvan-app1.nrsc.gov.in/api/geoid/curl_gdal_api.php"

# Bhuvan API token
api_token = "0c3613150a5574261d4b7bcf1286ba29ac419c24"

# Function to generate Python code for Bhuvan API request using OpenAI
def generate_bhuvan_api_code(id, datum):
    prompt = f"Generate Python code to download a zipped file from the Bhuvan API using the ID '{id}' and datum '{datum}'. The API token is '{api_token}'."
    prompt += f" The API URL for ellipsoid is '{base_url}?id={id}&datum={datum}&se=CDEM&key={api_token}', and for geoid is '{base_url}?id={id}&datum={datum}&se=CDEM&key={api_token}'."
    prompt += " Ensure the appropriate headers are set, such as 'Content-Type: application/zip' and 'Content-Disposition: attachment'. Use the requests library to make the GET request and save the downloaded zip file."

    # Make the OpenAI API call
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=300,
        n=1,
        stop=None,
    )

    # Extract and return the generated code
    generated_code = response["choices"][0]["text"]
    return generated_code

# Function to download zipped file from Bhuvan API using generated code
def download_file_using_generated_code(id, datum):
    generated_code = generate_bhuvan_api_code(id, datum)
    # Print or log the generated code for review
    print("Generated Code:")
    print(generated_code)

    # Execute the generated code
    exec(generated_code)

# Function for text-to-speech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Function for speech recognition
def takecommand():
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        return "none"
    return query


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

categories = [
    ("collaborators", "https://bhuvan.nrsc.gov.in/home/collabarators.php"),
    ("viewer", "https://bhuvan-app2.nrsc.gov.in/mgnrega/mgnrega_phase2.php"),
    ("darta", "https://bhuvan-app3.nrsc.gov.in/data/"),
    ("dimen", "https://bhuvan-app1.nrsc.gov.in/bhuvan2d/bhuvan/bhuvan2d.php"),
    ("ap", "https://bhuvan-app1.nrsc.gov.in/api/"),
    ("house", "https://bhuvan-app1.nrsc.gov.in/hfa/housing_for_all.php"),
    ("gg", "https://bhuvan.nrsc.gov.in/forum"),
    ("wb", "https://bhuvan-wbis.nrsc.gov.in/"),
    ("xx", "https://bhuvan-app1.nrsc.gov.in/pmgsy/home/index.php"),
    ("watr", "https://bhuvan-app1.nrsc.gov.in/mwrds/index.php"),
    ("aib", "https://bhuvan-app1.nrsc.gov.in/aibp/aibp.php"),
    ("nn", "https://bhuvan-app1.nrsc.gov.in/rkvy/index.php"),
    ("disaster", "https://bhuvan-app1.nrsc.gov.in/disaster/disaster.php?id=fire"),
    ("liv", "https://bhuvan-app1.nrsc.gov.in/cdma/index.php"),
    ("delt", "https://bhuvan-app1.nrsc.gov.in/deltas/index.php"),
    ("lol", "https://bhuvan-app1.nrsc.gov.in/agriculture/agri.php"),
    ("mines", "https://bhuvan-app1.nrsc.gov.in/mines/mines.php"),
    ("wueee", "https://bhuvan-app1.nrsc.gov.in/walamtari/walamtari.php"),
    ("road", "https://bhuvan-app1.nrsc.gov.in/toll/morth_nhai.php"),
    ("nuu", "https://bhuvan-app1.nrsc.gov.in/municipal/municipal.php"),
    ("noo", "https://bhuvan-app1.nrsc.gov.in/tourism/tourism.php?tourismid=1"),
    ("school", "https://bhuvan-app1.nrsc.gov.in/mhrd_ncert/sb/sb.php#school:NINTH"),
    ("cetg", "https://bhuvan-app1.nrsc.gov.in/sitemap/"),
    ("rbi", "https://bhuvan-app1.nrsc.gov.in/rbi"),
    ("store", "https://bhuvan-app1.nrsc.gov.in/2dresources/bhuvanstore.php"),
    ("cris", "https://bhuvan-app1.nrsc.gov.in/moef_cris"),
    ("coro", "https://bhuvan-app3.nrsc.gov.in/corona/"),
    ("child", "https://bhuvan-app1.nrsc.gov.in/anganwadi/"),
    ("pm", "https://bhuvan-app1.nrsc.gov.in/pmjvk"),
    ("obser", "https://bhuvan-app1.nrsc.gov.in/web_view/index.php"),
    ("saras", "https://bhuvan-app1.nrsc.gov.in/saraswati/"),
    ("hr", "https://bhuvan-app1.nrsc.gov.in/state/HR"),
    ("kf", "https://bhuvan-app1.nrsc.gov.in/ka_forest"),
    ("pf", "https://bhuvan-app1.nrsc.gov.in/pb_forest/"),
    ("tf", "https://bhuvan-app1.nrsc.gov.in/ts_forest/"),
    ("gang", "https://bhuvan-app1.nrsc.gov.in/mowr_ganga/"),
    ("hot", "https://bhuvan-app1.nrsc.gov.in/heatwave/"),
    ("FAM", "https://bhuvan-app1.nrsc.gov.in/pdmc/"),
    ("TOP", "https://bhuvan-app1.nrsc.gov.in/imd/"),
    ("HP", "https://bhuvan-app1.nrsc.gov.in/hp_forest/hpfd.php"),
    ("WEB", "https://bhuvan-app1.nrsc.gov.in/tourism/tourism.php"),
    ("NERT", "https://bhuvan-app1.nrsc.gov.in/mhrd_ncert/"),
    ("FLY", "https://bhuvan-app1.nrsc.gov.in/flycatchers/flycatchers.php"),
    ("GOG", "https://bhuvan-app1.nrsc.gov.in/geographicalindication/index.php"),
    ("HUM", "https://bhuvan-app1.nrsc.gov.in/mhrd_rusa/"),
    ("threedim", "https://bhuvan-app1.nrsc.gov.in/globe/3d.php"),
    ("hospi", "https://bhuvan-app1.nrsc.gov.in/ntr/"),
]

# Function to download file with progress bar
def download_with_progress(url, filename):
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024
    progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True)

    with open(filename, 'wb') as file, progress_bar:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)

def wishme():#cut
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning, what can I do for you?")
    elif 12 <= hour < 18:
        speak("Good afternoon, what can I do for you?")
    else:
        speak("Good evening, what can I do for you?")

# Example usage with voice commands


if __name__ == "__main__":  # last running programm
    wishme()
    while True:
        query =takecommand().lower()
        if "download" in query:
         while True:
           speak("it seems you need to download something feel free to say what do you want to download")
           command = takecommand()

           if "generate code to download the file" in command:
            speak("Sure, I will download the file. Please wait.")
            download_file_using_generated_code("cdnc43e", "ellipsoid")
            speak("File downloaded successfully.")
            os.startfile("cdnc43e.zip")  # Open the file location
            speak("click this link to download your file")
           elif "exit" in command or "quit" in command:
            speak("Exiting the program thank you for query Namaskar.")
           else:
            speak("not understanding you voice")
           break
        
        if "aditya" in query:                   
         pan=takecommand().lower()
         response=generate_response(pan)
         print(f"Aditya say:{response}")
         speak(response)
        for category, url in categories:
            for keyword in data_dictionary[category]:
                if keyword.lower() in query.lower():
                    webbrowser.open(url)
                    brief= f"give me the brief information about this website {url} in 100 words"
                    response=generate_response(brief)
                    print(f"Aditya say:{response}")
                    speak(response)
                    break
                break
            break
        
        if "tell me about" and "search for" in query:
            speak("searching...")
            query = query.replace("tell me about" or "search for", '')
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia" + results)
            break