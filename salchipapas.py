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
        st.subheader("¿¿Estas segura?? 🧐")
    elif st.session_state.intentos_no == 2:
        st.subheader("Vamos di que siiii 🙏✨")
    elif st.session_state.intentos_no == 3:
        st.subheader("Tu sabes que si quiereees 😏🍔")

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
            if st.session_state.intentos_no >= 4:
                st.session_state.paso = "pantalla_enojo"
            
            st.rerun()

# --- PASO 2: EL FLUJO DEL SÍ (PREGUNTAR POR EL LUGAR) ---
elif st.session_state.paso == "pregunta_lugar":
    st.success("Muchas graciaaaaaaaas :DDD 🎉")
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
    st.title("🚨 OK YA NO QUIERO NADA 😡😤")
    
    # Un texto mediano abajo para dar contexto dramático
    st.subheader("¡Te lo perdiste! 🙄💅")
    
    st.write("") # Espacio en blanco
    
    # Botón para que se arrepienta y vuelva a la pantalla del SÍ
    if st.button("Perdón, ¡sí quiero! 🥺", use_container_width=True):
        st.session_state.paso = "pregunta_lugar"
        st.rerun()
