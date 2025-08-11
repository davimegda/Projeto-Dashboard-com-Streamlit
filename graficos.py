import plotly.express as px
from utils import df_rec_estado, df_rec_mensal, df_rec_categoria, df_vendedores

# Gráfico Receita por Estado
grafico_map_estado = px.scatter_mapbox(
    df_rec_estado,
    lat='lat',
    lon='lon',
    size='Preço',
    hover_name='Local da compra',
    hover_data={'lat': False, 'lon': False},
    color_discrete_sequence=['#1f77b4'],
    zoom=2.8,  
    center={"lat": -14.2350, "lon": -51.9253},
    title='Receita por Estado'
)

grafico_map_estado.update_layout(
    mapbox_style='carto-positron', 
    margin={"r":0,"t":40,"l":0,"b":0}
)

# Gráfico Receita Mensal
grafico_rec_mensal = px.line(
    df_rec_mensal,
    x='Mês',
    y='Preço',
    markers=True,
    range_y=(0, df_rec_mensal.max()),
    color='Ano',
    line_dash='Ano',
    title='Receita Mensal'
)

grafico_rec_mensal.update_layout(yaxis_title = 'Receita')

grafico_rec_estado = px.bar(
    df_rec_estado.head(),
    x='Local da compra',
    y='Preço',
    text_auto=True,
    title='Top Receita por Estados'
)

# Gráfico Receita por Categoria
df_top5_categoria = df_rec_categoria.reset_index().head(5)

grafico_rec_categoria = px.bar(
    df_top5_categoria,
    x='Categoria do Produto',
    y='Preço',
    text=df_top5_categoria['Preço'].map('{:,.2f}'.format),
    title='Top 5 Categorias com Maior Receita',
    orientation='v',
    labels={'Preço': 'Receita (R$)', 'Categoria do Produto': 'Categoria'}
)

# Gráfico Receita Vendedores
df_vendedores_sorted = df_vendedores[['sum']].sort_values('sum', ascending=False).reset_index()

grafico_rec_vendedores = px.bar(
    df_vendedores_sorted,
    x='sum',
    y='Vendedor',  
    text=df_vendedores_sorted['sum'].map('{:,.2f}'.format),  # formatar números com 2 casas decimais e separador de milhares
    title='Receita por Vendedor',
    orientation='h',  
    labels={'sum': 'Receita (R$)', 'Vendedor': 'Vendedor'}
)

# Gráfico de Vendas por Vendedor
df_vendas_vendedores_sorted = df_vendedores.sort_values('count', ascending=False)
grafico_vendas_vendedores = px.bar(
    df_vendas_vendedores_sorted,
    x='count',
    y=df_vendas_vendedores_sorted.index,
    text_auto=True,
    title='Vendas por Vendedores',
    labels={'count': 'Quantidade de Vendas', 'y': 'Vendedor'}
)

