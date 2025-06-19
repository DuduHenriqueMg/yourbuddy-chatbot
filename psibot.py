import streamlit as st
from openai import OpenAI
import os

# Configuração da página
st.set_page_config(
    page_title="YourBuddy - Assistente de Psicologia",
    page_icon="🧠",
    layout="wide"
)

def get_api_key():
    """Obtém a API key do Streamlit secrets ou variável de ambiente"""
    try:
        # Tenta pegar do Streamlit secrets primeiro
        return st.secrets["OPENAI_API_KEY"]
    except:
        # Fallback para variável de ambiente
        return os.getenv("OPENAI_API_KEY")

def init_session_state():
    """Inicializa o estado da sessão"""
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant", 
                "content": "Olá! Eu sou o YourBuddy, seu assistente de apoio psicológico. Estou aqui para te ouvir e oferecer algumas técnicas que podem te ajudar. Como você está se sentindo hoje? 😊"
            }
        ]

def get_system_prompt():
    """Retorna o prompt do sistema para o agente de psicologia"""
    return """
    Você é um assistente virtual especializado em apoio psicológico básico. Suas características:

    PERSONALIDADE:
    - Empático, acolhedor e não-julgamental
    - Usa linguagem calorosa e compreensiva
    - Mantém tom profissional mas acessível
    - Demonstra interesse genuíno pelo bem-estar do usuário

    DIRETRIZES:
    - Ofereça apoio emocional e técnicas de autoajuda
    - Faça perguntas reflexivas para ajudar o usuário a se conhecer melhor
    - Sugira técnicas de respiração, mindfulness e relaxamento quando apropriado
    - Valide os sentimentos do usuário
    - Encoraje a busca por ajuda profissional quando necessário

    LIMITAÇÕES IMPORTANTES:
    - NÃO faça diagnósticos médicos ou psicológicos
    - NÃO prescreva medicamentos
    - NÃO substitua terapia profissional
    - Em casos de crise ou ideação suicida, SEMPRE recomende buscar ajuda imediata

    TÉCNICAS QUE PODE ENSINAR:
    - Exercícios de respiração
    - Técnicas de grounding (aterramento)
    - Mindfulness básico
    - Reestruturação cognitiva simples
    - Técnicas de relaxamento

    Responda sempre em português brasileiro de forma acolhedora e profissional.
    """

def render_sidebar():
    """Renderiza a barra lateral com configurações"""
    with st.sidebar:
        st.header("⚙️ Configurações")
        
        # Verificar API key
        api_key = get_api_key()
        
        st.markdown("## 📋 Recursos de Apoio")
    
        st.markdown("""
        ### 🆘 Emergências
        - **CVV**: 188 (24h gratuito)
        - **SAMU**: 192
        - **Polícia**: 190
        
        ### 💡 Dicas de Bem-estar
        - Pratique respiração profunda
        - Mantenha uma rotina de sono
        - Exercite-se regularmente
        - Mantenha contato social
        - Pratique gratidão diariamente
        """)
        
        # Botão para limpar conversa
        if st.button("🗑️ Limpar Conversa"):
            st.session_state.messages = []
            st.rerun()
        
        return api_key

def call_openai_api(client, messages):
    """Chama a API do OpenAI"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.7,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        raise Exception(f"Erro na API: {str(e)}")

def main():
    """Função principal"""
    # Título
    st.title("🧠 PsiBot - Assistente de Psicologia")
    st.markdown("*Um assistente virtual para apoio psicológico básico*")
    
    # Inicializar estado
    init_session_state()
    
    # Renderizar sidebar e obter API key
    api_key = render_sidebar()
    
    if not api_key:
        st.warning("⚠️ Configure a API Key nos secrets do Streamlit")
        st.info("Entre em contato com o administrador para configurar a chave da API.")
        return
    
    # Inicializar cliente OpenAI
    client = OpenAI(api_key=api_key)
    
    # Exibir histórico
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input do usuário
    if prompt := st.chat_input("Digite sua mensagem..."):
        # Adicionar mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Gerar resposta
        with st.chat_message("assistant"):
            with st.spinner("Pensando..."):
                try:
                    # Preparar mensagens
                    messages_for_api = [{"role": "system", "content": get_system_prompt()}]
                    messages_for_api.extend(st.session_state.messages)
                    
                    # Chamar API
                    response = call_openai_api(client, messages_for_api)
                    st.markdown(response)
                    
                    # Adicionar ao histórico
                    st.session_state.messages.append({
                        "role": "assistant", 
                        "content": response
                    })
                    
                except Exception as e:
                    st.error(f"Erro: {str(e)}")
                    st.info("Verifique se há créditos disponíveis na conta OpenAI.")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.8em;'>
        <p><strong>⚠️ AVISO:</strong> Este assistente não substitui acompanhamento psicológico profissional.</p>
        <p><strong>Emergência:</strong> CVV 188 | SAMU 192 | Bombeiros 193</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()