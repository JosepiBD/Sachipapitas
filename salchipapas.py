import streamlit as st

# Configuración de la página para que tenga un emoji lindo
st.set_page_config(page_title="¿Salchipapas? 🍟", page_icon="🍟")

# 1. INICIALIZAR LA MEMORIA (Session State)
# Si es la primera vez que se abre la página, definimos las variables de control
if "paso" not in st.session_state:
    st.session_state.paso = "pregunta_1"  # El paso inicial
if "intentos_no" not in st.session_state:
    st.session_state.intentos_no = 0       # Contador de cuántas veces dice que NO

import streamlit as st

# Configuración de la página
st.set_page_config(page_title="¿Salchipapas? 🍟", page_icon="🍟")

# 1. INICIALIZAR LA MEMORIA
if "paso" not in st.session_state:
    st.session_state.paso = "pregunta_1"
if "intentos_no" not in st.session_state:
    st.session_state.intentos_no = 0

# --- PASO 1: PREGUNTA INICIAL O CONTRA-PREGUNTAS DEL 'NO' ---
if st.session_state.paso == "pregunta_1":
    
    if st.session_state.intentos_no == 0:
        st.subheader("Me compras una salchipapa? 🥺")
    elif st.session_state.intentos_no == 1:
        st.subheader("Pero solo una salchipapa clasicaaaa :pp")
    elif st.session_state.intentos_no == 2:
        st.subheader("Vamos di que siiii 🙏✨")
    elif st.session_state.intentos_no == 3:
        st.subheader("Tu sabes que si quiereees 😏")
    elif st.session_state.intentos_no == 4:
        st.subheader("Y una salchipapititaa??🥺🥺")
    elif st.session_state.intentos_no == 5:
        st.subheader("Una salchipapitititita??🥺👅")
    elif st.session_state.intentos_no == 6:
        st.subheader("Solo las papitas y poquito hotdog?? 👅👅 ")
    elif st.session_state.intentos_no == 7:
        st.subheader("Solo papitaaas??🙂🙂")
    elif st.session_state.intentos_no == 8:
        st.subheader("Yaya una salchipapa de S/2 sin cremas :3")
    elif st.session_state.intentos_no == 9:
        st.subheader("Salchipapa de S/1 ???😔😔")
    elif st.session_state.intentos_no == 10:
        st.subheader("Tu te compras y me das 5 papitas y 2 hotdog😋😋😋")
    elif st.session_state.intentos_no == 11:
        st.subheader("Solo 4 papitas???😔😔")
    elif st.session_state.intentos_no == 12:
        st.subheader("3 papitaaa???😑😑")
    elif st.session_state.intentos_no == 13:
        st.subheader("1 papita????🙃🙃")
    elif st.session_state.intentos_no == 14:
        st.subheader("una pisca de papitas?🙃🙃🙃🙃")

    # Crear los dos botones
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SÍ", use_container_width=True):
            st.session_state.paso = "pregunta_lugar"
            st.rerun()

    with col2:
        if st.button("NO", use_container_width=True):
            st.session_state.intentos_no += 1
            
            # Si ya rechazó 4 veces (el inicial + 3 insistencias), va a la pantalla de enojo
            if st.session_state.intentos_no >= 15:
                st.session_state.paso = "pantalla_enojo"
            
            st.rerun()

# --- PASO 2: EL FLUJO DEL SÍ (PREGUNTAR POR EL LUGAR) ---
elif st.session_state.paso == "pregunta_lugar":
    st.success("Sabia que dirias que siii :DDD 🎉")
    st.write("¿De dónde me comprarás?")
    
    lugar = st.text_input("Escribe el lugar aquí:", placeholder="Ej. El carrito de la esquina...")
    
    if st.button("Continuar"):
        if lugar:
            st.session_state.lugar_elegido = lugar
            st.session_state.paso = "pantalla_final_si"
            st.rerun()
        else:
            st.warning("¡Tienes que escribir un lugar primero! 😮")

# --- PASO 3: RESPUESTA FINAL DEL SÍ ---
elif st.session_state.paso == "pantalla_final_si":
    lugar = st.session_state.lugar_elegido
    st.balloons()
    st.title(f"Entonces vamos a **{lugar}** y dime cuándo para comer una salchipapita :3 🍟❤️")
    
    if st.button("Reiniciar"):
        st.session_state.clear()
        st.rerun()

# --- PASO 4: PANTALLA FINAL DEL NO ---
elif st.session_state.paso == "pantalla_enojo":
    
    # st.title es el texto más grande nativo de Streamlit, 100% seguro contra errores
    st.title("OK YA NO QUIERO NADA :VVV")
    
    # Un texto mediano abajo para dar contexto dramático
    st.subheader("Yo que al final te iba invitar😒😒")
    
    st.write("") # Espacio en blanco
    
    # Botón para que se arrepienta y vuelva a la pantalla del SÍ
    if st.button("Perdón, ¡sí quiero! 🥺", use_container_width=True):
        st.session_state.paso = "pregunta_lugar"
        st.rerun()
