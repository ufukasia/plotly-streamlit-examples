param(
    [int]$Port = 8517
)

python -m streamlit run "app.py" --server.port $Port
