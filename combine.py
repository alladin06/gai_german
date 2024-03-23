import streamlit as st
from streamlit_option_menu import option_menu
# from main import main
from notes import notes_main
from enter_data import main_data
from app import nearby_hospi
from visualize_data import  track_progress_main
from acne import main_acne
from sayantan import sos_main
# from login import main_l

def main():

    PAGE_CONFIG = {"page_title": "Geriatric AI",
               "page_icon": "icon.png", "layout": "centered"}
    st.set_page_config(**PAGE_CONFIG)
    
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://img.freepik.com/premium-photo/green-background-with-bokeh-rays_582451-37.jpg");
    background-size: cover;
    background-position: oben links;
    background-repeat: nicht wiederholen;
    }}
    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
    st.sidebar.title("Geriatrische KI")
    menu = [ "Gesundheitsdatenaufzeichner", "Fortschritt verfolgen", "In der Nähe befindliche Krankenhäuser finden",  "SOS Alarm", "Notizen","Akneerkennung"]
    with st.sidebar:
        app_selection = option_menu(
        menu_title = None,
        options = menu,
        # icons = ['haus', 'zielscheibe', 'karte-checkliste', 'emoji-lächeln', 'journal']
    )
    # app_selection = st.sidebar.radio("Option auswählen", ["Daten","Medikamentenerinnerung", "Notizen", "In der Nähe befindliche Krankenhäuser finden", "Fortschritt verfolgen", "SOS Alarm"])

    if app_selection == "Medikamentenerinnerung":
        # main()
        pass
    # elif app_selection=="Anmelden":
    #     main_l()
        
    elif app_selection == "Notizen":
        notes_main()
    elif app_selection == "In der Nähe befindliche Krankenhäuser finden":
        nearby_hospi()
        # pass
    elif app_selection == "Fortschritt verfolgen":
        track_progress_main()
        # pass
    elif app_selection == "SOS Alarm":
        sos_main()
        # pass
    elif app_selection=="Gesundheitsdatenaufzeichner":
        # pass
        main_data()
    elif app_selection=="Akneerkennung":
        main_acne()

if __name__ == "__main__":
    main()
