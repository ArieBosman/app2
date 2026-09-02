# -*- coding: utf-8 -*-
"""
Rekentoets - interactieve quiz (Streamlit, variant 2)
Lokaal testen:  streamlit run app_variant2.py
"""

import streamlit as st

LETTERS = ["A", "B", "C", "D"]

QUESTIONS = [
    dict(q="Een plank is 2,4 meter lang. Hoeveel centimeter is dat?",
         opts=["24 cm", "240 cm", "2400 cm", "2,4 cm"], correct=1,
         worked="1 meter = 100 cm, dus 2,4 × 100 = 240 cm."),

    dict(q="Een fles bevat 1,25 liter limonade. Hoeveel milliliter is dat?",
         opts=["125 ml", "250 ml", "1250 ml", "12.500 ml"], correct=2,
         worked="1 liter = 1000 ml, dus 1,25 × 1000 = 1250 ml."),

    dict(q="Een hardloper doet 48 minuten over 12 km. Wat is zijn gemiddelde snelheid?",
         opts=["10 km/u", "12 km/u", "15 km/u", "18 km/u"], correct=2,
         worked="48 min = 0,8 uur. Snelheid = 12 : 0,8 = 15 km/u."),

    dict(q="Een kamer is 3,6 m breed en 4,2 m lang. Wat is de oppervlakte?",
         opts=["7,8 m²", "12,6 m²", "15,12 m²", "18,2 m²"], correct=2,
         worked="Oppervlakte = 3,6 × 4,2 = 15,12 m²."),

    dict(q="Een doos heeft afmetingen 20 × 15 × 10 cm. Wat is de inhoud?",
         opts=["300 cm³", "3000 cm³", "30000 cm³", "300000 cm³"], correct=1,
         worked="Inhoud = 20 × 15 × 10 = 3000 cm³."),

    dict(q="Een grafiek begint bij 50 in plaats van bij 0 op de y-as. Wat is het effect?",
         opts=["Geen effect", "De stijging lijkt kleiner", "De stijging lijkt groter", "De grafiek wordt onleesbaar"],
         correct=2,
         worked="Door de y-as niet bij 0 te laten beginnen, lijken verschillen groter: de stijging lijkt groter."),

    dict(q="Een auto rijdt 180 km in 2 uur en 15 minuten. Wat is de gemiddelde snelheid?",
         opts=["60 km/u", "72 km/u", "80 km/u", "90 km/u"], correct=2,
         worked="2 uur 15 min = 2,25 uur. 180 : 2,25 = 80 km/u."),

    dict(q="Een winkel verhoogt een prijs van 40 euro met 12%. Wat is de nieuwe prijs?",
         opts=["44,80 euro", "45,20 euro", "47,60 euro", "52,00 euro"], correct=0,
         worked="12% van 40 = 4,80. Nieuwe prijs = 40 + 4,80 = 44,80 euro."),

    dict(q="Een bedrag van 250 euro wordt met 15% verlaagd. Wat is de nieuwe prijs?",
         opts=["212,50 euro", "215,00 euro", "225,00 euro", "235,50 euro"], correct=0,
         worked="15% van 250 = 37,50. Nieuwe prijs = 250 - 37,50 = 212,50 euro."),

    dict(q="Wat is 3/5 als decimaal getal?",
         opts=["0,35", "0,5", "0,6", "0,75"], correct=2,
         worked="3 gedeeld door 5 = 0,6."),

    dict(q="Wat is 0,75 als breuk in eenvoudigste vorm?",
         opts=["1/2", "3/4", "2/3", "4/5"], correct=1,
         worked="0,75 = 75/100 = 3/4."),

    dict(q="Een kaart heeft schaal 1 : 25.000. Een afstand is 8 cm op de kaart. Hoeveel km is dat in werkelijkheid?",
         opts=["2 km", "4 km", "8 km", "20 km"], correct=0,
         worked="8 × 25.000 = 200.000 cm. 200.000 cm = 2 km."),

    dict(q="Een machine verbruikt 0,8 kWh per uur. Hoeveel kWh verbruikt hij in 6 uur?",
         opts=["3,2 kWh", "4,8 kWh", "5,6 kWh", "6,8 kWh"], correct=1,
         worked="0,8 × 6 = 4,8 kWh."),

    dict(q="Een rechthoek heeft een omtrek van 34 cm. De lengte is 10 cm. Wat is de breedte?",
         opts=["7 cm", "8 cm", "12 cm", "14 cm"], correct=0,
         worked="Omtrek = 2(l + b). 34 = 2(10 + b) → 17 = 10 + b → b = 7 cm."),

    dict(q="Een klas heeft 28 leerlingen. 25% is afwezig. Hoeveel leerlingen zijn dat?",
         opts=["5", "6", "7", "8"], correct=2,
         worked="25% van 28 = 0,25 × 28 = 7 leerlingen."),

    dict(q="Een cilinder heeft straal 4 cm en hoogte 10 cm. Wat is de inhoud?",
         opts=["40π cm³", "80π cm³", "120π cm³", "160π cm³"], correct=3,
         worked="Inhoud = π × r² × h = π × 16 × 10 = 160π cm³."),

    dict(q="Een bedrag stijgt van 120 naar 150 euro. Wat is de procentuele stijging?",
         opts=["20%", "25%", "30%", "35%"], correct=1,
         worked="Stijging = 30. 30/120 × 100% = 25%."),

    dict(q="Een fiets kost 360 euro. Na korting betaal je 306 euro. Hoeveel procent korting is dat?",
         opts=["10%", "12%", "15%", "20%"], correct=2,
         worked="Korting = 360 - 306 = 54. 54/360 × 100% = 15%."),

    dict(q="Een rechthoek heeft lengte 12 cm en breedte 3 cm. Wat is de lengte van de diagonaal (afgerond)?",
         opts=["12,4 cm", "12,6 cm", "13 cm", "15 cm"], correct=0,
         worked="Diagonaal = √(12² + 3²) = √153 ≈ 12,37 cm, afgerond ≈ 12,4 cm."),

    dict(q="Een tank bevat 45 liter benzine. De auto verbruikt 7,5 liter per 100 km. Hoe ver kun je rijden?",
         opts=["300 km", "450 km", "600 km", "750 km"], correct=2,
         worked="45 ÷ 7,5 = 6. 6 × 100 km = 600 km."),

    dict(q="Een taart wordt verdeeld in 12 stukken. Je eet 3 stukken. Welk percentage van de taart is dat?",
         opts=["15%", "20%", "25%", "30%"], correct=2,
         worked="3/12 = 0,25 = 25%."),

    dict(q="Een grafiek toont een daling van 80 naar 64. Wat is de procentuele daling?",
         opts=["10%", "15%", "20%", "25%"], correct=2,
         worked="Daling = 16. 16/80 × 100% = 20%."),

    dict(q="Een verhouding is 5 : 8. Wat is de breukvorm van deze verhouding?",
         opts=["5/8", "8/5", "3/5", "5/3"], correct=0,
         worked="5 : 8 schrijf je als breuk 5/8."),

    dict(q="Een kubus heeft ribbe 6 cm. Wat is de inhoud?",
         opts=["36 cm³", "72 cm³", "216 cm³", "256 cm³"], correct=2,
         worked="Inhoud kubus = 6³ = 216 cm³."),

    dict(q="Een bedrag wordt vermenigvuldigd met factor 1,12. Wat betekent dat?",
         opts=["12% daling", "12% stijging", "blijft gelijk", "wordt gedeeld door 12"], correct=1,
         worked="Factor 1,12 betekent: het bedrag wordt met 12% verhoogd.")
]

TEAL = "#1B6D6D"

st.set_page_config(page_title="Rekentoets - interactieve quiz (variant 2)", page_icon="🧮", layout="centered")

# ---------- Sessiestatus initialiseren ----------
if "answers" not in st.session_state:
    st.session_state.answers = [{"choice": None, "work": ""} for _ in QUESTIONS]
if "index" not in st.session_state:
    st.session_state.index = 0
if "finished" not in st.session_state:
    st.session_state.finished = False

st.markdown(f"<h1 style='color:{TEAL};'>Rekentoets - interactieve quiz (variant 2)</h1>", unsafe_allow_html=True)


def question_screen():
    i = st.session_state.index
    item = QUESTIONS[i]
    saved = st.session_state.answers[i]

    st.progress((i + 1) / len(QUESTIONS))
    st.markdown(f"**Vraag {i + 1} van {len(QUESTIONS)}**")
    st.write(item["q"])

    option_labels = [f"{LETTERS[j]}.  {opt}" for j, opt in enumerate(item["opts"])]
    default_index = saved["choice"] if saved["choice"] is not None else None
    choice = st.radio("Kies een antwoord:", options=list(range(4)),
                      format_func=lambda j: option_labels[j],
                      index=default_index, key=f"choice_{i}")

    work = st.text_area(
        "Uitwerking (laat je berekening/redenering zien - levert een extra punt op, "
        "ook als het antwoord fout is):",
        value=saved["work"], key=f"work_{i}", height=120)

    col1, col2 = st.columns(2)
    with col1:
        if i > 0 and st.button("< Vorige"):
            saved["choice"], saved["work"] = choice, work
            st.session_state.index -= 1
            st.rerun()
    with col2:
        label = "Resultaten tonen" if i == len(QUESTIONS) - 1 else "Volgende >"
        if st.button(label):
            saved["choice"], saved["work"] = choice, work
            if i == len(QUESTIONS) - 1:
                st.session_state.finished = True
            else:
                st.session_state.index += 1
            st.rerun()


def results_screen():
    st.markdown(f"<h2 style='color:{TEAL};'>Resultaten</h2>", unsafe_allow_html=True)

    correct_count = 0
    extra_points = 0

    for i, item in enumerate(QUESTIONS):
        ans = st.session_state.answers[i]
        is_correct = ans["choice"] == item["correct"]
        if is_correct:
            correct_count += 1

        with st.container(border=True):
            gekozen = LETTERS[ans["choice"]] if ans["choice"] is not None else "(geen antwoord)"
            status = "juist" if is_correct else "fout"
            st.markdown(f"**Vraag {i + 1} - jouw antwoord: {gekozen} ({status}) - "
                        f"goed antwoord: {LETTERS[item['correct']]}**")
            st.write(item["q"])

            if ans["work"]:
                st.caption("Jouw uitwerking:")
                st.info(ans["work"])
            else:
                st.caption("(geen uitwerking ingevuld)")

            st.caption("Modeluitwerking: " + item["worked"])

            extra = st.checkbox("Uitwerking correct/volledig -> extra punt toekennen",
                                key=f"extra_{i}")
            if extra:
                extra_points += 1

    max_score = len(QUESTIONS) * 2
    total = correct_count + extra_points
    st.markdown("---")
    st.markdown(
        f"### Score: {correct_count}/{len(QUESTIONS)} juiste antwoorden + {extra_points} extra "
        f"punt(en) voor uitwerking = **{total}/{max_score} punten**")

    if st.button("Opnieuw beginnen"):
        st.session_state.answers = [{"choice": None, "work": ""} for _ in QUESTIONS]
        st.session_state.index = 0
        st.session_state.finished = False
        st.rerun()


if st.session_state.finished:
    results_screen()
else:
    question_screen()
