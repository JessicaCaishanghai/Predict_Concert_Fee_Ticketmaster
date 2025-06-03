import streamlit as st



# 事件类型
event_types = ['Arts & Theatre', 'Sports', 'Music', 'Miscellaneous']

# 每个 event_type 对应的子类别
event_subsections = {
    'Music': [
        'Reggae', 'Rock', 'Country', 'R&B', 'Pop', 'Dance/Electronic',
        'Latin', 'Other', 'Blues', 'Metal', 'Undefined', 'World',
        'Hip-Hop/Rap', 'Jazz', 'Alternative', 'Folk', 'Religious', 'Classical', 'Holiday'
    ],
    'Arts & Theatre': [
        'Fine Art', 'Magic & Illusion', 'Comedy',
       'Circus & Specialty Acts', 'Miscellaneous Theatre', 'Theatre',
       'Performance Art', 'Dance', 'Spectacular', 'Variety',
       'Classical', "Children's Theatre"
    ],
    'Sports': [
        'Soccer', 'Baseball', 'Equestrian', 'Motorsports/Racing',
       'Football', 'Volleyball', 'Rodeo', 'Basketball', 'Miscellaneous',
       'Golf', 'Lacrosse', 'Martial Arts'
    ],
    'Miscellaneous': [
        'Psychics/Mediums/Hypnotists', 'Undefined', 'Family',
       'Community/Civic', 'Food & Drink', 'Ice Shows',
       'Hobby/Special Interest Expos', 'Fairs & Festivals'
    ]

    event_type = st.selectbox('Select Event Type:', event_types)

    st.write(f'You selected Event Type: {event_type}')