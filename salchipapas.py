import streamlit as st

# Configuración de la página para que tenga un emoji lindo
st.set_page_config(page_title="¿Salchipapas? 🍟", page_icon="🍟")

# 1. INICIALIZAR LA MEMORIA (Session State)
# Si es la primera vez que se abre la página, definimos las variables de control
if "paso" not in st.session_state:
    st.session_state.paso = "pregunta_1"  # El paso inicial
if "intentos_no" not in st.session_state:
    st.session_state.intentos_no = 0       # Contador de cuántas veces dice que NO

# --- PASO 1: PREGUNTA INICIAL O CONTRA-PREGUNTAS DEL 'NO' ---
if st.session_state.paso == "pregunta_1":
    
    # Cambiamos la pregunta o frase según cuántas veces haya presionado NO
    if st.session_state.intentos_no == 0:
        st.subheader("Me compras una salchipapa? 🥺")
    elif st.session_state.intentos_no == 1:
        st.subheader("¿¿Estas segura?? 🧐")
    elif st.session_state.intentos_no == 2:
        st.subheader("Vamos di que siiii 🙏✨")
    elif st.session_state.intentos_no == 3:
        st.subheader("Tu sabes que si quiereees 😏🍔")

    # Crear los dos botones en paralelo
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SÍ", use_container_width=True):
            st.session_state.paso = "pregunta_lugar"  # Avanza al flujo del SÍ
            st.rerun() # Recarga la página inmediatamente para mostrar el cambio

    with col2:
        if st.button("NO", use_container_width=True):
            st.session_state.intentos_no += 1  # Sumamos un intento fallido
            
            # Si ya rechazó 4 veces (el inicial + 3 insistencias), va a la pantalla final de enojo
            if st.session_state.intentos_no >= 4:
                st.session_state.paso = "pantalla_enojo"
            
            st.rerun()

# --- PASO 2: EL FLUJO DEL SÍ (PREGUNTAR POR EL LUGAR) ---
elif st.session_state.paso == "pregunta_lugar":
    st.success("Muchas graciaaaaaaaas :DDD 🎉")
    st.write("¿De dónde me comprarás?")
    
    # Barra para escribir el lugar
    lugar = st.text_input("Escribe el lugar aquí:", placeholder="Ej. El carrito de la esquina, McDonald's...")
    
    if st.button("Continuar"):
        if lugar:  # Verificamos que no lo deje vacío
            st.session_state.lugar_elegido = lugar
            st.session_state.paso = "pantalla_final_si"
            st.rerun()
        else:
            st.warning("¡Tienes que escribir un lugar primero! 😮")

# --- PASO 3: RESPUESTA FINAL DEL SÍ ---
elif st.session_state.paso == "pantalla_final_si":
    # Recuperamos el lugar guardado en la memoria
    lugar = st.session_state.lugar_elegido
    
    st.balloons() # ¡Efecto de globos celebrando! 🎈
    st.title(f"Entonces vamos a **{lugar}** y dime cuándo para comer una salchipapita :3 🍟❤️")
    
    # Botón por si quieren reiniciar el juego
    if st.button("Reiniciar"):
        st.session_state.clear()
        st.rerun()

# --- PASO 4: PANTALLA FINAL DEL NO (OK YA NO QUIERO NADA) ---
elif st.session_state.paso == "pantalla_enojo":
    # Ponemos el título gigante usando formato HTML h1 personalizado
    st.markdown("<h1 style='text-align: center; color: red; font-size: 60px;'>OK YA NO QUIERO NADA 😡😤</h1>", unsafe_html=True)
    
    # Botón de arrepentimiento para darle otra oportunidad
    if st.button("Perdón, ¡sí quiero!🥺"):
        st.session_state.paso = "pregunta_lugar"
        st.rerun()
