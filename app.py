import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('Model.pkl','rb'))

Cars = pd.read_csv('Cars_datasets.csv')
def get_brand_name(cars_data):
    return cars_data.split(' ')[0].strip()

Cars["brand"] = Cars["name"].apply(get_brand_name)

brand_images = {
    "Maruti": "https://images-saboomaruti-in.s3.ap-south-1.amazonaws.com/new_baleno/2.webp",
    "Hyundai": "https://wallpapercave.com/wp/wp8143800.jpg",
    "Ford": "https://images.hdqwalls.com/wallpapers/ford-shelby-gt500.jpg",
    "Honda": "https://wallpapercave.com/wp/wp1919674.jpg",
    "Toyota": "https://wallpapers.com/images/hd/lights-reflected-at-toyota-supra-car-nrgbgyssrc84qaco.jpg",
    "BMW": "https://wallpaperaccess.com/full/2264749.jpg",
    "Mercedes-Benz": "https://images.hdqwalls.com/wallpapers/green-mercedes-benz-amg-gt-ww.jpg",
    "Skoda": "https://wallpaperaccess.com/full/2055846.jpg",
    "Renault": "https://wallpaperaccess.com/full/1271177.png",
    "Mahindra": "https://4kwallpapers.com/images/wallpapers/mahindra-thar-roxx-1920x1080-18214.jpg",
    "Tata": "https://wallpapercave.com/wp/wp6700499.png",
    "Chevrolet": "https://images.hdqwalls.com/download/2023-camaro-special-edition-f4-2560x1024.jpg",
    "Datsun": "https://wallpapercrafter.com/desktop1/608834-Nissan-S30-Nissan-Fairlady-Z-Datsun-240Z-Japanese.jpg",
    "Jeep": "https://rare-gallery.com/mocahbig/1372296-2021-Wrangler-Unlimited-Rubicon-392-Jeep-SUV-Light.jpg",
    "Mitsubishi": "https://wallpapercave.com/wp/wp9189939.jpg",
    "Audi": "https://car-images.bauersecure.com/wp-images/3193/audi_r8_200.jpg",
    "Volkswagen": "https://cdn.myportfolio.com/61781da2-87cb-4b7f-9cca-a68f193cae6c/86d07747-7b8a-48da-ab90-b81e839426f6_rwc_0x192x1920x1082x1920.jpg?h=e7c4c8959bd7c1ea939c3e610d688318",
    "Nissan": "https://wallpaperaccess.com/full/280367.jpg",
    "Lexus": "https://wallpapercave.com/wp/wp3065084.jpg",
    "Jaguar": "https://wallpaperaccess.com/full/1687651.jpg",
    "Land": "https://wallpaperaccess.com/full/2103935.jpg",
    "MG": "https://wallpapercave.com/wp/wp10401727.jpg",
    "Volvo": "https://wallpaperbat.com/img/168805-volvo-s60-polestar-front-hd-wallpaper.jpg",
    "Daewoo": "https://i.pinimg.com/originals/b3/8f/a4/b38fa4723c4428f210db668daad3db1c.jpg",
    "Kia": "https://wallpaperaccess.com/full/2325484.jpg",
    "Fiat": "https://images.wallpaperscraft.com/image/single/abarth_fiat_front_view_black_109779_3840x2160.jpg",
    "Force": "https://wallpapercave.com/wp/wp10525925.jpg",
    "Ambassador": "https://wallpapercave.com/wp/wp8898345.jpg",
    "Ashok": "https://wallpapercave.com/wp/wp4152807.jpg",
    "Isuzu": "https://www.hdcarwallpapers.com/walls/arctic_trucks_isuzu_d_max_at35_safir_double_cab_2019_4k-HD.jpg",
    "Opel": "https://www.opel-uae.com/content/dam/opel/master/experience-opel/concept-cars/OPEL_GT_Motiv_16x9_02_v02_jg_sRGB.jpg"
}

def set_background(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def add_glow_effect():
    st.markdown(
        """
        <style>
        /* Make the selectbox glow red */
        div[data-baseweb="select"] > div {
            border: 2px solid red !important;
            box-shadow: 0px 0px 10px red !important;
            border-radius: 10px !important; /* Make rounded corners */
            transition: 0.3s;
        }
        div[data-baseweb="select"]:hover > div {
            box-shadow: 0px 0px 20px red !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_glow_effect()

st.markdown("""
    <style>
        /* Stylish glowing title with transparent background */
        .title-glow {
            font-size: 45px;
            font-weight: bold;
            color: black;
            text-align: center;
            padding: 10px;
            border-radius: 10px;
            text-shadow: 3px 3px 10px rgba(255, 255, 255, 0.7);
            position: fixed;
            width: 100%;
            top: 40px; /* Adjusted to lower the title */
            left: 0;
            z-index: 1000;
            background: rgba(0, 0, 0, 0.2); /* Semi-transparent background */
        }
        
        /* Push content down so it's not hidden behind the title */
        .stApp {
            padding-top: 100px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="title-glow">Car Price Prediction</h1>', unsafe_allow_html=True)


brand_options = ["Select a Car Brand"] + list(Cars["brand"].unique())

st.markdown(
    """
    <style>
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="glow-text">Select Your Car Brand:</p>', unsafe_allow_html=True)

# Select box without extra space
selected_brand = st.selectbox("", brand_options, key="brand_select", label_visibility="collapsed")

if selected_brand in brand_images:
    set_background(brand_images[selected_brand])
elif selected_brand == "Select a Car Brand":
    set_background("https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/e55186115813417.605578275cf66.jpg")

def add_glow_effect():
    st.markdown(
        """
        <style>
        /* Glowing effect for number input container */
        div[data-testid="stNumberInput"] {
            border: 2px solid red !important;
            box-shadow: 0px 0px 15px red !important;
            border-radius: 10px !important;
            transition: 0.3s;
            margin: 0px !important;
            padding: 0px !important;
        }
        div[data-testid="stNumberInput"]:hover {
            box-shadow: 0px 0px 25px red !important;
        }

        /* Black text shadow effect (Your Provided Code) */
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_glow_effect()

st.markdown('<p class="glow-text">Car Manufactured Year (1994 - 2024):</p>', unsafe_allow_html=True)

selected_year = st.number_input("", min_value=1994, max_value=2024, value=2015, step=1, key="year_select", label_visibility="collapsed")

def add_glow_effect():
    st.markdown(
        """
        <style>
        /* Glowing effect for number input container */
        div[data-testid="stNumberInput"] {
            border: 2px solid red !important;
            box-shadow: 0px 0px 15px red !important;
            border-radius: 10px !important;
            transition: 0.3s;
            margin: 0px !important;
            padding: 0px !important;
        }
        div[data-testid="stNumberInput"]:hover {
            box-shadow: 0px 0px 25px red !important;
        }

        /* Black text shadow effect (Your Provided Code) */
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_glow_effect()

st.markdown('<p class="glow-text">Number of kms Driven (11 - 200000):</p>', unsafe_allow_html=True)

selected_km = st.number_input("", min_value=11, max_value=200000, value=5000, step=1, key="km_select", label_visibility="collapsed")

st.markdown(
    """
    <style>
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="glow-text">Fuel Type:</p>', unsafe_allow_html=True)

selected_fuel = st.selectbox("", Cars['fuel'].unique(), key="fuel_type", label_visibility="collapsed")

st.markdown(
    """
    <style>
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="glow-text">Seller Type:</p>', unsafe_allow_html=True)

selected_seller = st.selectbox("", Cars['seller_type'].unique(), key="seller_type", label_visibility="collapsed")

st.markdown(
    """
    <style>
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="glow-text">Transmission Type:</p>', unsafe_allow_html=True)

selected_transmission = st.selectbox("", Cars['transmission'].unique(), key="transmission_type", label_visibility="collapsed")

st.markdown(
    """
    <style>
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<p class="glow-text">Owner Type:</p>', unsafe_allow_html=True)

selected_owner = st.selectbox("", Cars['owner'].unique(), key="owner_type", label_visibility="collapsed")

def add_glow_effect():
    st.markdown(
        """
        <style>
        /* Glowing effect for number input container */
        div[data-testid="stNumberInput"] {
            border: 2px solid red !important;
            box-shadow: 0px 0px 15px red !important;
            border-radius: 10px !important;
            transition: 0.3s;
            margin: 0px !important;
            padding: 0px !important;
        }
        div[data-testid="stNumberInput"]:hover {
            box-shadow: 0px 0px 25px red !important;
        }

        /* Black text shadow effect (Your Provided Code) */
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_glow_effect()

st.markdown('<p class="glow-text">Car Mileage (10 - 40):</p>', unsafe_allow_html=True)

selected_mileage = st.number_input("", min_value=10, max_value=40, value=10, step=1, key="mileage_select", label_visibility="collapsed")

def add_glow_effect():
    st.markdown(
        """
        <style>
        /* Glowing effect for number input container */
        div[data-testid="stNumberInput"] {
            border: 2px solid red !important;
            box-shadow: 0px 0px 15px red !important;
            border-radius: 10px !important;
            transition: 0.3s;
            margin: 0px !important;
            padding: 0px !important;
        }
        div[data-testid="stNumberInput"]:hover {
            box-shadow: 0px 0px 25px red !important;
        }

        /* Black text shadow effect (Your Provided Code) */
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_glow_effect()

st.markdown('<p class="glow-text">Engine CC (700 - 5000):</p>', unsafe_allow_html=True)

selected_CC = st.number_input("", min_value=700, max_value=5000, value=700, step=1, key="CC_select", label_visibility="collapsed")

def add_glow_effect():
    st.markdown(
        """
        <style>
        /* Glowing effect for number input container */
        div[data-testid="stNumberInput"] {
            border: 2px solid red !important;
            box-shadow: 0px 0px 15px red !important;
            border-radius: 10px !important;
            transition: 0.3s;
            margin: 0px !important;
            padding: 0px !important;
        }
        div[data-testid="stNumberInput"]:hover {
            box-shadow: 0px 0px 25px red !important;
        }

        /* Black text shadow effect (Your Provided Code) */
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_glow_effect()

st.markdown('<p class="glow-text">Max Power (0 - 200):</p>', unsafe_allow_html=True)

selected_power = st.number_input("", min_value=0, max_value=200, value=50, step=1, key="power_select", label_visibility="collapsed")

def add_glow_effect():
    st.markdown(
        """
        <style>
        /* Glowing effect for number input container */
        div[data-testid="stNumberInput"] {
            border: 2px solid red !important;
            box-shadow: 0px 0px 15px red !important;
            border-radius: 10px !important;
            transition: 0.3s;
            margin: 0px !important;
            padding: 0px !important;
        }
        div[data-testid="stNumberInput"]:hover {
            box-shadow: 0px 0px 25px red !important;
        }

        /* Black text shadow effect (Your Provided Code) */
        .glow-text {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-shadow: 0 0 3px black, 0 0 6px black, 0 0 9px black;
            margin: 0px;
            padding: 0px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_glow_effect()

st.markdown('<p class="glow-text">No of Seats (5 - 10):</p>', unsafe_allow_html=True)

selected_seats = st.number_input("", min_value=5, max_value=10, value=5, step=1, key="seats_select", label_visibility="collapsed")

st.markdown("""
    <style>
        div.stButton > button {
            width: 100%;
            font-size: 30px;
            font-weight: bold;
            padding: 15px;
            border-radius: 10px;
            background-color: #ff4b4b;
            color: white;
            border: 3px solid #ff4b4b;
            transition: 0.3s;
            box-shadow: 0 0 10px #ff4b4b;
        }
        div.stButton > button:hover {
            background-color: black;
            border: 3px solid white;
            box-shadow: 0 0 20px white;
        }
        .prediction-text {
            font-size: 60px;
            font-weight: bold;
            color: white;
            text-align: center;
            margin-top: 30px;
            padding: 20px;
            background: linear-gradient(to right, #ff4b4b, #ff2e2e);
            border-radius: 15px;
            text-shadow: 3px 3px 20px rgba(255, 255, 255, 0.8);
            box-shadow: 0px 0px 25px rgba(255, 75, 75, 0.9);
        }
    </style>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    predict = st.button("Predict Car Price")

if predict:
    try:
        if not selected_brand:
            st.markdown(f'<p class="prediction-text">Select the car</p>', unsafe_allow_html=True)
        else:
            input_data_model = pd.DataFrame([
                [selected_brand, selected_year, selected_km, selected_fuel, selected_seller,
                 selected_transmission, selected_owner, selected_mileage, selected_CC, selected_power, selected_seats]
            ], columns=['name', 'year', 'km_driven', 'fuel', 'seller_type', 'transmission',
                        'owner', 'mileage', 'engine', 'max_power', 'seats'])

            mappings = {
                'owner': {'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth & Above Owner': 4, 'Test Drive Car': 5},
                'fuel': {'Diesel': 1, 'Petrol': 2, 'LPG': 3, 'CNG': 4},
                'seller_type': {'Individual': 1, 'Dealer': 2, 'Trustmark Dealer': 3},
                'transmission': {'Manual': 1, 'Automatic': 2},
                'name': {brand: idx+1 for idx, brand in enumerate([
                    'Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault', 'Mahindra',
                    'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz', 'Mitsubishi', 'Audi',
                    'Volkswagen', 'BMW', 'Nissan', 'Lexus', 'Jaguar', 'Land', 'MG', 'Volvo',
                    'Daewoo', 'Kia', 'Fiat', 'Force', 'Ambassador', 'Ashok', 'Isuzu', 'Opel'])}
            }

            for col, mapping in mappings.items():
                input_data_model[col].replace(mapping, inplace=True)

            Car_price = model.predict(input_data_model)
            st.markdown(f'<p class="prediction-text">Estimated Car Price: ₹ {Car_price[0]:,.2f}</p>', unsafe_allow_html=True)
    except Exception as e:
        st.markdown(f'<p class="prediction-text">Please Select The Car To Predict Price</p>', unsafe_allow_html=True)
