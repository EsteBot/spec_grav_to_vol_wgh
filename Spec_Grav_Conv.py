import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

# CSS to center the elements
st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Centering the headers
st.markdown("<h2 class='center' style='color:rgb(80, 200, 120);'>An EsteStyle Streamlit Page<br>Where Python Wiz Meets Data Viz!</h2>", unsafe_allow_html=True)
st.markdown("<h2 class='center'></h2>", unsafe_allow_html=True)

st.markdown("<img src='https://1drv.ms/i/s!ArWyPNkF5S-foZspwsary83MhqEWiA?embed=1&width=307&height=307' width='300' style='display: block; margin: 0 auto;'>" , unsafe_allow_html=True)

st.markdown("<h2 class='center'></h2>", unsafe_allow_html=True)

st.markdown("<h2 class='center' style='color: rgb(80, 200, 120);'>Specific Gravity to<br>Dilution Volumes & Weights</h2>", unsafe_allow_html=True)

st.markdown("<h2 class='center'></h2>", unsafe_allow_html=True)

st.markdown("<h3 class='center' style='color: gold;'>🐱Originally created at the University of Colorado Denver 🐾</h3>" , unsafe_allow_html=True)
st.markdown("<h3 class='center' style='color: gold;'>🧪In the Bland Laboratory for Behavioral Neuroscience🧠</h3>", unsafe_allow_html=True)
st.markdown("<h3 class='center' style='color: rgb(80, 200, 120);'>🤖By Esteban C Loetz 💾</h3>" , unsafe_allow_html=True)

st.markdown("<h1 class='center'></h1>", unsafe_allow_html=True)

def specific_gravity_converter(s_grv_input, s_vol_input, f_vol_input):
    h2o_vol = round(f_vol_input - ((s_vol_input / 100) * f_vol_input), 2)
    sol_vol = round((s_vol_input / 100) * f_vol_input, 2)
    sol_wgt = round(s_grv_input * sol_vol, 2)
    vol_wgt = round(h2o_vol + sol_wgt, 2)

    # Define colors for the graph
    h2o_color = '#66b3ff'
    solute_color = '#ff9999'
    
    # Use the placeholder to create new columns for the output
    with output_placeholder:
        col4, col5 = st.columns(2)

        with col4:
            # Display H2O and Solute Volumes with matching colors in Streamlit
            st.markdown(f"<h5 style='color: {h2o_color};'>H2O Volume (mL) needed: {h2o_vol}</h5>", unsafe_allow_html=True)
            st.markdown(f"<h5 style='color: {solute_color};'>Solute Volume (mL) needed: {sol_vol}</h5>", unsafe_allow_html=True)
            st.write(f"Total volume (mL) of solution is: {f_vol_input}")

            # Doughnut chart data
            vols = [h2o_vol, sol_vol]
            total_vol = round(sum(vols), 2)
            labels_vol = [f'H2O Vol: {h2o_vol}', f'Solute Vol: {sol_vol}']
            colors = [h2o_color, solute_color]  # Use your custom colors here!

            # Create doughnut chart
            fig, ax = plt.subplots(figsize=(6, 6))
            wedges, texts, autotexts = ax.pie(
                vols, labels=labels_vol, colors=colors, startangle=90,
                wedgeprops=dict(width=0.5), autopct='%1.1f%%',
                textprops={'color': 'white'}  # Label text color inside the chart
            )

            # Set label colors manually to match the input text
            for text, color in zip(texts, colors):
                text.set_color(color)

            # Add a white circle at the center to create the doughnut hole
            center_circle = plt.Circle((0, 0), 0.20, fc='white')
            fig.gca().add_artist(center_circle)

            # Display the total value in the center of the doughnut
            plt.text(0, 0, f'Total\n{total_vol}', horizontalalignment='center', verticalalignment='center', fontsize=12)

            # Display the chart in Streamlit
            st.pyplot(fig)

            # Display volume calculations
            h2o_pct = (100 - s_vol_input) / 100
            solute_pct = (s_vol_input / 100)
            st.write("Volume Calculations:")
            st.write("Volume = Percent(%) * Final Volume(mL)")
            st.write(f"Final H2O Vol = {h2o_pct} * {f_vol_input}")
            st.write(f"Final Solute Vol = {solute_pct} * {f_vol_input}")

        with col5:
            # Display H2O and Solute Weights with matching colors in Streamlit
            st.markdown(f"<h5 style='color: {h2o_color};'>H2O weight (grams) in the solution is: {h2o_vol}</h5>", unsafe_allow_html=True)
            st.markdown(f"<h5 style='color: {solute_color};'>Solute weight (grams) in the solution is: {sol_wgt}</h5>", unsafe_allow_html=True)
            st.write(f"Total weight (grams) of the final solution is: {vol_wgt}")

            # Doughnut chart data
            wgts = [h2o_vol, sol_wgt]
            total_wgt = round(sum(wgts), 2)
            labels_wgt = [f'H2O Weight: {h2o_vol}', f'Solute Weight: {sol_wgt}']
            colors = [h2o_color, solute_color]  # Use your custom colors here!

            # Create doughnut chart
            fig, ax = plt.subplots(figsize=(6, 6))
            wedges, texts, autotexts = ax.pie(
                wgts, labels=labels_wgt, colors=colors, startangle=90,
                wedgeprops=dict(width=0.5), autopct='%1.1f%%',
                textprops={'color': 'white'}  # Label text color inside the chart
            )

            # Set label colors manually to match the input text
            for text, color in zip(texts, colors):
                text.set_color(color)

            # Add a white circle at the center to create the doughnut hole
            center_circle = plt.Circle((0, 0), 0.20, fc='white')
            fig.gca().add_artist(center_circle)

            # Display the total value in the center of the doughnut
            plt.text(0, 0, f'Total\n{total_wgt}', horizontalalignment='center', verticalalignment='center', fontsize=12)

            # Display the chart in Streamlit
            st.pyplot(fig)

            # Display weight calculations
            st.write("Weight Calculations")
            st.write("Weight = Specific Gravity(g/mL) * Individual Volume(mL)")
            st.write(f"Final H2O Weight = 1 * {h2o_vol}")
            st.write(f"Final Solute Weight = {s_grv_input} * {sol_vol}")

# Initial set of columns for input fields and button
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    s_grv_input = st.number_input("Enter the specific gravity of the liquid to be diluted into H2O (g/mL):", 
                                value=0.0, step=0.1, format="%.2f")

    s_vol_input = st.number_input("Enter the target percent (Vol/Vol) of the above liquid to be in the solution (%):", 
                                value=0.0, step=0.1, format="%.2f")

    f_vol_input = st.number_input("Enter the target final volume of solution that will be generated (mL):", 
                                value=0.0, step=0.1, format="%.2f")
    
    calc_button = st.button("Press to convert the entered values into their volumes & weights")
    st.write('')

# Placeholder outside the input columns for the results and charts
output_placeholder = st.empty()

if calc_button:
    # Check if any input is zero and display an error message
    if s_grv_input == 0 or s_vol_input == 0 or f_vol_input == 0:
        st.error("Error: Please enter a value greater than 0 for all fields.")
    else:
        specific_gravity_converter(s_grv_input, s_vol_input, f_vol_input)






