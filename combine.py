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
    menu = [ "Gesundheitsdatenaufzeichner", "Fortschritt verfolgen", "In der Nähe befindliche Krankenhäuser finden",  "SOS Alarm", "Notizen","Akneerkennung","Veranstaltungen in meiner Nähe"]
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
    elif app_selection == "Veranstaltungen in meiner Nähe":st.markdown("""
    **Online-Veranstaltung**: Digivartti: Thema ist Google Kalender  
    **Wann:** Fr, 20.9.2024 von 10 bis 10.30 Uhr  
    **Wo:** Online via Zoom  
    [Mehr Informationen](https://www.entersenior.fi/tapahtumat/digivartti-0924/)

    **Lokale Veranstaltung**: Lösungen für ein gutes Alltagsleben  
    **Wann:** Mi-Do, 2-3.10.2024  
    **Wo:** Messezentrum Helsinki, Messuaukio 1, 00520 Helsinki  
    [Mehr Informationen](https://hyvaika.expomark.fi/)

    **Reise:** Nordportugal, Porto und Portweingüter  
    **Wann:** Mo-Sa, 21-26.10.2024  
    **Wo:** Porto, Portugal  
    [Mehr Informationen](https://kilta.senioriliitto.fi/Tapahtumat/tapahtumatiedot.aspx?id=28261)

    **Hybrid-Veranstaltung:** Erkenne einen Online-Betrug  
    **Wann:** Mi, 23.10.2024 von 13:30 bis 15:00 Uhr  
    **Wo:** Online via Zoom, Veranstaltung im Kampi  
    [Mehr Informationen](https://www.entersenior.fi/tapahtumat/tunnista-nettihuijaus/)

    **Lokale Veranstaltung:** Geführtes Training im Fitnessstudio  
    **Wann:** Mo, 30.12.2024 von 10:00 bis 11:00 Uhr  
    **Wo:** Seniorenzentrum Myllypuro/Dienstleistungszentrum, Myllymatkantie 4, Helsinki  
    [Mehr Informationen](https://tapahtumat.hel.fi/fi/events/helsinki:agh3rorroe)
    """)


if __name__ == "__main__":
    main()
