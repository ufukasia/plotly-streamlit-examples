from __future__ import annotations

import json

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.utils import PlotlyJSONEncoder


TAB_LABELS = [
    "`01_fark.py`",
    "`02_express.py`",
    "`03_mimari.py`",
    "`04_secim.py`",
    "`05_zaman.py`",
    "`06_hiyerarsi.py`",
    "`07_dashboard.py`",
]


def configure_page() -> None:
    st.set_page_config(
        page_title="Hafta 7 | Plotly Laboratuvari",
        page_icon="P",
        layout="wide",
        initial_sidebar_state="collapsed",
    )


def inject_css() -> None:
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(circle at top left, rgba(245, 213, 71, 0.18), transparent 28%),
                    radial-gradient(circle at top right, rgba(27, 114, 242, 0.14), transparent 24%),
                    linear-gradient(180deg, #f7f1e6 0%, #f4f6f9 42%, #eef3f8 100%);
            }

            .block-container {
                padding-top: 1.2rem;
                padding-bottom: 2rem;
                max-width: 1400px;
            }

            div[data-baseweb="tab-list"] {
                gap: 0.2rem;
                padding: 0.25rem 0.35rem 0;
                border-bottom: 1px solid rgba(89, 103, 128, 0.18);
            }

            button[data-baseweb="tab"] {
                background: #ebe2d0;
                border: 1px solid rgba(79, 91, 117, 0.26);
                border-bottom: none;
                border-radius: 12px 12px 0 0;
                color: #334155;
                font-family: "Consolas", "Fira Code", monospace;
                font-size: 0.94rem;
                min-height: 3rem;
                padding: 0.5rem 0.95rem;
            }

            button[data-baseweb="tab"][aria-selected="true"] {
                background: #fffdf8;
                color: #0f172a;
                box-shadow: 0 -4px 0 #d97706 inset;
            }

            div[data-baseweb="tab-panel"] {
                background: rgba(255, 255, 255, 0.72);
                border: 1px solid rgba(79, 91, 117, 0.18);
                border-top: none;
                border-radius: 0 0 18px 18px;
                padding: 1rem 1rem 0.8rem;
                backdrop-filter: blur(3px);
            }

            .hero-card {
                background: linear-gradient(135deg, rgba(255,255,255,0.92), rgba(255,248,236,0.92));
                border: 1px solid rgba(79, 91, 117, 0.18);
                border-radius: 22px;
                padding: 1.3rem 1.5rem 1.1rem;
                box-shadow: 0 12px 40px rgba(15, 23, 42, 0.08);
                margin-bottom: 1rem;
            }

            .hero-kicker {
                letter-spacing: 0.08em;
                text-transform: uppercase;
                font-size: 0.76rem;
                color: #b45309;
                font-weight: 700;
            }

            .hero-title {
                font-size: 2rem;
                line-height: 1.1;
                font-weight: 800;
                color: #0f172a;
                margin: 0.35rem 0 0.5rem;
            }

            .hero-subtitle {
                font-size: 1.02rem;
                color: #334155;
                max-width: 72rem;
            }

            .chip-row {
                display: flex;
                flex-wrap: wrap;
                gap: 0.45rem;
                margin-top: 0.9rem;
            }

            .chip {
                background: #fff7ed;
                border: 1px solid rgba(180, 83, 9, 0.22);
                border-radius: 999px;
                color: #9a3412;
                font-size: 0.84rem;
                font-weight: 600;
                padding: 0.28rem 0.72rem;
            }

            .section-card {
                background: rgba(255, 255, 255, 0.86);
                border: 1px solid rgba(79, 91, 117, 0.16);
                border-radius: 18px;
                padding: 1rem 1rem 0.9rem;
                margin-bottom: 0.9rem;
            }

            .section-step {
                color: #b45309;
                font-size: 0.8rem;
                font-weight: 800;
                text-transform: uppercase;
                letter-spacing: 0.08em;
            }

            .section-title {
                color: #0f172a;
                font-size: 1.55rem;
                font-weight: 800;
                margin: 0.25rem 0 0.35rem;
            }

            .section-summary {
                color: #334155;
                font-size: 0.98rem;
                margin-bottom: 0;
            }

            .note-card {
                background: linear-gradient(180deg, rgba(243, 244, 246, 0.96), rgba(255,255,255,0.96));
                border: 1px solid rgba(79, 91, 117, 0.15);
                border-left: 5px solid #d97706;
                border-radius: 16px;
                padding: 0.95rem 1rem 0.8rem;
                margin-bottom: 0.9rem;
            }

            .note-title {
                font-size: 0.95rem;
                font-weight: 800;
                color: #0f172a;
                margin-bottom: 0.45rem;
            }

            .note-card ul {
                margin: 0;
                padding-left: 1rem;
                color: #334155;
            }

            .mini-architecture {
                background: #0f172a;
                color: #e2e8f0;
                border-radius: 18px;
                padding: 1rem;
                border: 1px solid rgba(148, 163, 184, 0.18);
                margin-bottom: 0.8rem;
            }

            .mini-architecture strong {
                color: #fbbf24;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_hero() -> None:
    st.markdown(
        """
        <div class="hero-card">
            <div class="hero-kicker">Veri Görselleştirme | Hafta 7</div>
            <div class="hero-title">Plotly Laboratuvarı: Etkileşimli Görselleştirme Mimarisi</div>
            <p class="hero-subtitle">
                Bu sayfa, sınıfta adım adım ilerleyebileceğiniz yerel bir öğretim arayüzüdür.
                Soldan sağa ilerleyin: önce neden etkileşim gerektiğini gösterin, sonra Plotly Express,
                figür mimarisi, seçim olayları, zaman serileri, hiyerarşik yapı ve en sonda web bileşeni mantığına geçin.
            </p>
            <div class="chip-row">
                <span class="chip">Statik sistemden farkı vurgula</span>
                <span class="chip">İkonik Plotly örnekleri göster</span>
                <span class="chip">Kullanıcı etkileşimini canlı yaşat</span>
                <span class="chip">Dash mantığına köprü kur</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.caption("Sekmeler bilerek dosya adı gibi etiketlendi; sınıfta soldan sağa ilerlemeniz için.")


def render_section_header(step: str, title: str, summary: str) -> None:
    st.markdown(
        f"""
        <div class="section-card">
            <div class="section-step">{step}</div>
            <div class="section-title">{title}</div>
            <p class="section-summary">{summary}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_note_card(title: str, items: list[str]) -> None:
    item_markup = "".join(f"<li>{item}</li>" for item in items)
    st.markdown(
        f"""
        <div class="note-card">
            <div class="note-title">{title}</div>
            <ul>{item_markup}</ul>
        </div>
        """,
        unsafe_allow_html=True,
    )


@st.cache_data
def load_gapminder() -> pd.DataFrame:
    return px.data.gapminder().query("year >= 1972").copy()


@st.cache_data
def load_iris() -> pd.DataFrame:
    iris = px.data.iris().copy()
    iris["row_id"] = np.arange(len(iris))
    return iris


@st.cache_data
def load_monthly_channels() -> pd.DataFrame:
    months = pd.date_range("2025-09-01", periods=10, freq="MS")
    data = pd.DataFrame(
        {
            "ay": np.tile(months, 3),
            "kanal": np.repeat(["Web", "Mobil", "Mağaza"], len(months)),
            "gelir": [
                82,
                88,
                91,
                95,
                103,
                110,
                118,
                123,
                127,
                133,
                70,
                76,
                81,
                85,
                94,
                98,
                101,
                108,
                112,
                119,
                45,
                49,
                51,
                54,
                59,
                63,
                65,
                69,
                72,
                74,
            ],
        }
    )
    return data


@st.cache_data
def load_latency_data() -> pd.DataFrame:
    rng = np.random.default_rng(42)
    timestamps = pd.date_range("2026-03-01", periods=240, freq="h")
    baseline = 118 + 10 * np.sin(np.linspace(0, 8 * np.pi, len(timestamps)))
    noise = rng.normal(0, 4.5, len(timestamps))
    latency = baseline + noise
    latency[70:78] += np.linspace(18, 62, 8)
    latency[150:156] += np.linspace(15, 45, 6)

    df = pd.DataFrame({"zaman": timestamps, "gecikme_ms": latency.round(1)})
    df["hareketli_ortalama"] = df["gecikme_ms"].rolling(12, min_periods=1).mean().round(1)
    df["olay"] = ""
    df.loc[df.index[74], "olay"] = "Cache devre dışı kaldı"
    df.loc[df.index[153], "olay"] = "Arka plan job yükü yükseldi"
    return df


@st.cache_data
def load_hierarchy_data() -> pd.DataFrame:
    rows = [
        ("Türkiye", "E-Ticaret", "Elektronik", "Kulaklık", 28),
        ("Türkiye", "E-Ticaret", "Elektronik", "Klavye", 21),
        ("Türkiye", "E-Ticaret", "Ev", "Lamba", 16),
        ("Türkiye", "E-Ticaret", "Ev", "Masa", 11),
        ("Türkiye", "Saha Satışı", "Kurumsal", "Lisans", 34),
        ("Türkiye", "Saha Satışı", "Kurumsal", "Bakım", 24),
        ("Türkiye", "Saha Satışı", "Perakende", "POS", 14),
        ("Türkiye", "Saha Satışı", "Perakende", "Aksesuar", 9),
    ]
    hierarchy = pd.DataFrame(
        rows,
        columns=["ülke", "kanal", "kategori", "ürün", "gelir_milyon"],
    )
    hierarchy["büyüme"] = [12, 7, 15, 5, 18, 10, 8, 4]
    return hierarchy


@st.cache_data
def load_dashboard_data() -> pd.DataFrame:
    rng = np.random.default_rng(7)
    months = pd.date_range("2025-10-01", periods=6, freq="MS")
    regions = ["Ankara", "İstanbul", "İzmir"]
    segments = ["Kurumsal", "KOBİ", "Bireysel"]
    channels = ["Web", "Mobil", "Saha"]

    rows: list[dict[str, object]] = []
    for month in months:
        for region in regions:
            for segment in segments:
                for channel in channels:
                    revenue = rng.integers(35, 95)
                    margin = rng.uniform(0.12, 0.34)
                    rows.append(
                        {
                            "ay": month,
                            "bölge": region,
                            "segment": segment,
                            "kanal": channel,
                            "gelir": int(revenue),
                            "adet": int(revenue * rng.uniform(7, 11)),
                            "marj": round(float(margin), 3),
                        }
                    )
    return pd.DataFrame(rows)


def build_channel_story_figure() -> go.Figure:
    df = load_monthly_channels()
    fig = px.line(
        df,
        x="ay",
        y="gelir",
        color="kanal",
        markers=True,
        title="Kanal Bazlı Gelir Akışı",
        labels={"ay": "Ay", "gelir": "Gelir (milyon TL)", "kanal": "Kanal"},
        template="plotly_white",
    )
    fig.update_layout(
        hovermode="x unified",
        legend_title_text="",
        margin=dict(t=60, l=10, r=10, b=10),
    )
    fig.add_vrect(
        x0="2026-01-01",
        x1="2026-02-01",
        fillcolor="orange",
        opacity=0.10,
        line_width=0,
        annotation_text="kampanya penceresi",
        annotation_position="top left",
    )
    return fig


def build_gapminder_figure(continent_filter: list[str], log_x: bool) -> go.Figure:
    df = load_gapminder()
    filtered = df[df["continent"].isin(continent_filter)]
    fig = px.scatter(
        filtered,
        x="gdpPercap",
        y="lifeExp",
        animation_frame="year",
        animation_group="country",
        size="pop",
        color="continent",
        hover_name="country",
        log_x=log_x,
        size_max=55,
        range_y=[25, 90],
        title="İkonik Plotly Örneği: Hareketli Küresel Gelişim Grafiği",
        labels={
            "gdpPercap": "Kişi başına gelir",
            "lifeExp": "Yaşam beklentisi",
            "pop": "Nüfus",
            "continent": "Kıta",
        },
        template="plotly_white",
    )
    fig.update_layout(margin=dict(t=70, l=10, r=10, b=10))
    return fig


def build_express_vs_go_figures() -> tuple[go.Figure, go.Figure]:
    df = load_monthly_channels()
    summary = (
        df.groupby(["ay", "kanal"], as_index=False)["gelir"]
        .sum()
        .sort_values(["kanal", "ay"])
    )

    express_fig = px.line(
        summary,
        x="ay",
        y="gelir",
        color="kanal",
        markers=True,
        title="Plotly Express: veri çerçevesinden hızlı figür",
        labels={"ay": "Ay", "gelir": "Gelir", "kanal": "Kanal"},
        template="plotly_white",
    )
    express_fig.update_layout(hovermode="x unified", legend_title_text="")

    go_fig = go.Figure()
    palette = {"Web": "#2563eb", "Mobil": "#d97706", "Mağaza": "#059669"}
    for channel, chunk in summary.groupby("kanal"):
        go_fig.add_trace(
            go.Scatter(
                x=chunk["ay"],
                y=chunk["gelir"],
                mode="lines+markers",
                name=channel,
                line=dict(width=3, color=palette[channel]),
            )
        )
    go_fig.update_layout(
        title="Graph Objects: iz bazında inşa edilen figür",
        template="plotly_white",
        hovermode="x unified",
        legend_title_text="",
        xaxis_title="Ay",
        yaxis_title="Gelir",
    )

    return express_fig, go_fig


def preview_values(value: object) -> object:
    if value is None:
        return []
    if isinstance(value, dict):
        if "bdata" in value and "dtype" in value:
            return {"encoded": True, "dtype": value["dtype"]}
        return {key: preview_values(item) for key, item in list(value.items())[:3]}
    if isinstance(value, np.ndarray):
        return value[:3].tolist()
    if isinstance(value, (list, tuple, pd.Series, pd.Index)):
        return list(value[:3])
    if hasattr(value, "tolist"):
        try:
            converted = value.tolist()
            if isinstance(converted, list):
                return converted[:3]
            return converted
        except Exception:
            return str(value)
    return value


def figure_tree_excerpt(fig: go.Figure) -> str:
    fig_dict = fig.to_dict()
    excerpt = {
        "data": [
            {
                "type": trace.get("type"),
                "name": trace.get("name"),
                "x": preview_values(trace.get("x", [])),
                "y": preview_values(trace.get("y", [])),
            }
            for trace in fig_dict["data"][:2]
        ],
        "layout": {
            "title": fig_dict["layout"].get("title"),
            "hovermode": fig_dict["layout"].get("hovermode"),
            "legend": fig_dict["layout"].get("legend"),
        },
        "frames": fig_dict.get("frames", []),
    }
    return json.dumps(excerpt, ensure_ascii=False, indent=2, cls=PlotlyJSONEncoder)


def extract_selected_indices(event: object) -> list[int]:
    if event is None:
        return []
    selection = getattr(event, "selection", None)
    if not selection:
        return []

    points = selection.get("points", [])
    indices: set[int] = set()
    for point in points:
        point_index = point.get("point_index")
        if point_index is not None:
            indices.add(int(point_index))
            continue
        custom_data = point.get("customdata", [])
        if custom_data:
            indices.add(int(custom_data[0]))
    return sorted(indices)


def render_tab_difference() -> None:
    render_section_header(
        "Adım 1",
        "Statik grafik ile etkileşimli grafik arasındaki kopuş",
        "Dersi burada başlatın: aynı veri artık tek kare bir çıktı değil, kullanıcının soru sorabildiği canlı bir yüzeydir.",
    )

    left, right = st.columns([0.9, 1.35], gap="large")
    with left:
        st.metric("Öğrenciye ilk cümle", "Grafik artık arayüz bileşeni", "Statikten etkileşime")
        render_note_card(
            "Bu tabda özellikle vurgulayın",
            [
                "Statik sistemler çoğunlukla son görüntüyü üretir; Plotly görünüm ile veri ilişkisini canlı tutar.",
                "Hover, legend toggle ve zoom yeni soru üretmenin araçlarıdır; süs değildir.",
                "Kullanıcı, raporu okumaz; grafik üstünde keşif yapar.",
            ],
        )
        render_note_card(
            "Sınıfta sorulabilecek kısa sorular",
            [
                "Tek bir zirve noktasını statik grafikte nasıl anlatırsınız, interaktif grafikte nasıl gösterirsiniz?",
                "Bir seriyi geçici olarak kapatmak neden analitik olarak değerlidir?",
                "Bu grafiği PDF yerine canlı göstermek hangi soruları mümkün kılar?",
            ],
        )

    with right:
        fig = build_channel_story_figure()
        st.plotly_chart(
            fig,
            use_container_width=True,
            theme=None,
            config={"displaylogo": False, "scrollZoom": True},
        )
        st.caption(
            "Öğrencilerden şunu yapmalarını isteyin: bir kanalı legend'dan kapatsınlar, sonra kampanya penceresine zoom yapsınlar ve hover ile ay bazlı farkı okusunlar."
        )


def render_tab_express() -> None:
    render_section_header(
        "Adım 2",
        "Plotly Express: ikonik örnekle hızlı giriş",
        "İlk güçlü demo için hareketli bubble chart kullanın. Plotly'nin neden akılda kaldığını öğrenciler burada anlar.",
    )

    controls_col, chart_col = st.columns([0.85, 1.4], gap="large")
    with controls_col:
        continents = sorted(load_gapminder()["continent"].unique().tolist())
        selected = st.multiselect(
            "Kıtaları seçin",
            continents,
            default=continents,
            help="Kısıtlayıp aynı figürün nasıl yeniden anlamlandığını gösterin.",
        )
        log_x = st.toggle("Gelir eksenini log ölçeğe al", value=True)

        render_note_card(
            "Bu örnekte hangi kavramları anlatın?",
            [
                "Bir veri çerçevesinden birkaç satırla çok katmanlı görselleştirme üretmek.",
                "Animasyon karesinin zaman bilgisini taşıması.",
                "Bubble size, color, hover ve slider'ın tek figürde birleşmesi.",
            ],
        )

        st.code(
            """fig = px.scatter(
    df, x="gdpPercap", y="lifeExp",
    animation_frame="year",
    size="pop", color="continent"
)""",
            language="python",
        )

    with chart_col:
        if not selected:
            st.warning("En az bir kıta seçin.")
            return

        fig = build_gapminder_figure(selected, log_x)
        st.plotly_chart(
            fig,
            use_container_width=True,
            theme=None,
            config={"displaylogo": False},
        )
        st.caption(
            "Öğrenciye şu cümleyi kurdurun: 'Bu figür tek bir görsel değil; zaman, nüfus, kıta ve gelir ilişkisini aynı arayüzde taşıyan bir keşif nesnesi.'"
        )


def render_tab_architecture() -> None:
    render_section_header(
        "Adım 3",
        "Figür mimarisi: Express, Graph Objects ve figure ağacı",
        "Bu tab, Plotly'nin neden sadece çizim API'si değil bir figür modeli olduğunu gösterir.",
    )

    express_fig, go_fig = build_express_vs_go_figures()
    mode = st.radio(
        "Aynı veriyi hangi pencereden göstereyim?",
        ["Plotly Express", "Graph Objects", "Figure Ağacı"],
        horizontal=True,
    )

    left, right = st.columns([1.25, 0.95], gap="large")
    with left:
        if mode == "Plotly Express":
            st.plotly_chart(
                express_fig,
                use_container_width=True,
                theme=None,
                config={"displaylogo": False},
            )
            st.code(
                """px.line(df, x="ay", y="gelir", color="kanal",
markers=True, title="Hızlı prototip")""",
                language="python",
            )
        elif mode == "Graph Objects":
            st.plotly_chart(
                go_fig,
                use_container_width=True,
                theme=None,
                config={"displaylogo": False},
            )
            st.code(
                """fig = go.Figure()
fig.add_trace(go.Scatter(...))
fig.update_layout(...)
fig.show()""",
                language="python",
            )
        else:
            st.code(figure_tree_excerpt(go_fig), language="json")

    with right:
        st.markdown(
            """
            <div class="mini-architecture">
                <strong>Figure</strong><br/>
                ├── data: trace listesi<br/>
                ├── layout: başlık, eksen, legend, tema<br/>
                └── frames: animasyon için ardışık durumlar
            </div>
            """,
            unsafe_allow_html=True,
        )
        render_note_card(
            "Bu tabda öğretim hedefi",
            [
                "Express hız içindir, Graph Objects kontrol içindir.",
                "Her iki yol da aynı figure ağacına çıkar.",
                "data, layout ve frames ayrımı web tabanlı taşınabilirliğin temelidir.",
            ],
        )
        render_note_card(
            "Kritik cümle",
            [
                "Plotly figürü, JSON'a serileştirilebilen bir nesnedir; bu yüzden Python'dan tarayıcıya doğal köprü kurar."
            ],
        )


def render_tab_selection() -> None:
    render_section_header(
        "Adım 4",
        "Seçim olayları: kullanıcı artık veriyi işaretleyebilir",
        "Bu bölümde interaktivite görünür hale gelir: kutu veya lasso ile seçilen noktalar başka özetleri günceller.",
    )

    iris = load_iris()
    scatter = px.scatter(
        iris,
        x="sepal_width",
        y="sepal_length",
        color="species",
        size="petal_length",
        hover_name="species",
        custom_data=["row_id", "petal_width"],
        title="Iris Dağılımı: Seçim ile alt kümeyi keşfet",
        labels={
            "sepal_width": "Sepal width",
            "sepal_length": "Sepal length",
            "petal_length": "Petal length",
            "species": "Tür",
        },
        template="plotly_white",
    )
    scatter.update_layout(dragmode="lasso", legend_title_text="")

    left, right = st.columns([1.2, 0.95], gap="large")
    with left:
        st.caption("Grafik üstünde box veya lasso ile seçim yapın. Seçim otomatik olarak bu sekmeyi yeniden hesaplar.")
        event = st.plotly_chart(
            scatter,
            key="iris_selection_chart",
            use_container_width=True,
            theme=None,
            on_select="rerun",
            selection_mode=("points", "box", "lasso"),
            config={"displaylogo": False},
        )
    with right:
        selected_indices = extract_selected_indices(event)
        selected_df = iris.iloc[selected_indices] if selected_indices else iris
        selected_count = len(selected_df)
        st.metric("Seçili nokta sayısı", selected_count)
        if selected_indices:
            st.success("Seçim algılandı. Sağdaki özetler seçilen alt kümeye göre güncellendi.")
        else:
            st.info("Henüz seçim yok. Şu anda tüm veri kümesini görüyorsunuz.")

        summary = (
            selected_df.groupby("species", as_index=False)
            .size()
            .rename(columns={"size": "adet"})
        )
        bar = px.bar(
            summary,
            x="species",
            y="adet",
            color="species",
            title="Seçili alt kümede tür dağılımı",
            template="plotly_white",
        )
        bar.update_layout(showlegend=False, margin=dict(t=50, l=10, r=10, b=10))
        st.plotly_chart(
            bar,
            use_container_width=True,
            theme=None,
            config={"displaylogo": False},
        )
        st.dataframe(
            selected_df[["species", "sepal_width", "sepal_length", "petal_width"]]
            .head(8)
            .rename(
                columns={
                    "species": "Tür",
                    "sepal_width": "Sepal width",
                    "sepal_length": "Sepal length",
                    "petal_width": "Petal width",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )

    render_note_card(
        "Bu tabın mesajı",
        [
            "st.plotly_chart seçim olaylarını Streamlit içinde input gibi davranacak şekilde kullanabilir.",
            "Grafik üstünde yapılan işaretleme başka bileşenleri güncelliyorsa, artık görsel sadece çıktı değil giriş de üretir.",
            "Bu mantık öğrenciyi Dash callback kavramına hazırlar.",
        ],
    )


def render_tab_timeseries() -> None:
    render_section_header(
        "Adım 5",
        "Zaman serisinde hover, range slider ve anotasyon",
        "Geçen haftanın çizgi mantığını bu hafta etkileşimli zaman penceresi ve olay açıklamasıyla yeniden okutun.",
    )

    df = load_latency_data()
    show_avg = st.toggle("12 saatlik hareketli ortalamayı göster", value=True)
    show_incidents = st.toggle("Olay anotasyonlarını göster", value=True)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=df["zaman"],
            y=df["gecikme_ms"],
            mode="lines",
            name="Ham sinyal",
            line=dict(color="#2563eb", width=2),
        )
    )
    if show_avg:
        fig.add_trace(
            go.Scatter(
                x=df["zaman"],
                y=df["hareketli_ortalama"],
                mode="lines",
                name="12 saatlik ortalama",
                line=dict(color="#d97706", width=3),
            )
        )

    if show_incidents:
        incidents = df[df["olay"] != ""]
        for _, row in incidents.iterrows():
            fig.add_vline(x=row["zaman"], line_dash="dash", line_color="#ef4444", opacity=0.65)
            fig.add_annotation(
                x=row["zaman"],
                y=row["gecikme_ms"],
                text=row["olay"],
                showarrow=True,
                arrowhead=2,
                ay=-45,
                bgcolor="rgba(255,255,255,0.9)",
            )

    fig.update_layout(
        title="Sunucu gecikmesi: olay, gürültü ve temel yönü birlikte oku",
        template="plotly_white",
        hovermode="x unified",
        legend_title_text="",
        xaxis_title="Zaman",
        yaxis_title="Gecikme (ms)",
        margin=dict(t=60, l=10, r=10, b=10),
    )
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=[
                dict(count=24, label="24s", step="hour", stepmode="backward"),
                dict(count=72, label="3g", step="hour", stepmode="backward"),
                dict(step="all", label="Hepsi"),
            ]
        ),
    )

    left, right = st.columns([1.28, 0.92], gap="large")
    with left:
        st.plotly_chart(
            fig,
            use_container_width=True,
            theme=None,
            config={"displaylogo": False},
        )
    with right:
        st.metric("Maksimum gecikme", f"{df['gecikme_ms'].max():.1f} ms")
        st.metric("Ortalama gecikme", f"{df['gecikme_ms'].mean():.1f} ms")
        st.metric("Olay sayısı", int((df["olay"] != "").sum()))
        render_note_card(
            "Bu tabda vurgulayın",
            [
                "Range slider, kullanıcının inceleme penceresini değiştirmesini sağlar.",
                "Hovermode='x unified' seri karşılaştırmasını kolaylaştırır.",
                "Anotasyon, hikâye anlatımını grafiğin içine taşır; ayrı açıklama metnine mecbur bırakmaz.",
            ],
        )


def render_tab_hierarchy() -> None:
    render_section_header(
        "Adım 6",
        "Treemap ve sunburst: aynı hiyerarşi, farklı geometri",
        "Plotly yalnızca çizgi ve scatter için değil; hiyerarşik ilişkileri etkileşimli açmak için de güçlüdür.",
    )

    data = load_hierarchy_data()
    min_revenue = st.slider("En düşük gelir eşiği", min_value=0, max_value=34, value=9)
    chart_type = st.radio(
        "Görsel türü",
        ["Treemap", "Sunburst"],
        horizontal=True,
    )
    filtered = data[data["gelir_milyon"] >= min_revenue]

    if chart_type == "Treemap":
        fig = px.treemap(
            filtered,
            path=["ülke", "kanal", "kategori", "ürün"],
            values="gelir_milyon",
            color="büyüme",
            color_continuous_scale="Blues",
            title="Treemap: alan verimliliği ile parça-bütün okuması",
        )
    else:
        fig = px.sunburst(
            filtered,
            path=["ülke", "kanal", "kategori", "ürün"],
            values="gelir_milyon",
            color="büyüme",
            color_continuous_scale="Sunset",
            title="Sunburst: derinlik hissi ile katmanlı okuma",
        )
    fig.update_layout(template="plotly_white", margin=dict(t=60, l=10, r=10, b=10))

    left, right = st.columns([1.18, 0.98], gap="large")
    with left:
        st.plotly_chart(
            fig,
            use_container_width=True,
            theme=None,
            config={"displaylogo": False},
        )
    with right:
        render_note_card(
            "Bu tabda öğretim akışı",
            [
                "Önce kullanıcıya hover yaptırın; üst-alt yol bilgisini okutun.",
                "Aynı veri Treemap'te alan, Sunburst'te halka derinliği ile konuşur.",
                "Statik raporda yer darlığı nedeniyle zorlaşan hiyerarşik okuma burada etkileşimle açılır.",
            ],
        )
        st.dataframe(
            filtered.sort_values("gelir_milyon", ascending=False)
            .rename(
                columns={
                    "ülke": "Ülke",
                    "kanal": "Kanal",
                    "kategori": "Kategori",
                    "ürün": "Ürün",
                    "gelir_milyon": "Gelir (M)",
                    "büyüme": "Büyüme",
                }
            ),
            use_container_width=True,
            hide_index=True,
        )


def render_tab_dashboard() -> None:
    render_section_header(
        "Adım 7",
        "Grafikten web bileşenine: küçük bir dashboard mantığı",
        "Bu son sekme, Plotly'nin neden yalnızca figür değil uygulama parçası olduğunu gösterir. Buradan Dash callback fikrine bağlanın.",
    )

    df = load_dashboard_data()
    controls = st.columns(3)
    with controls[0]:
        region = st.selectbox("Bölge", sorted(df["bölge"].unique().tolist()))
    with controls[1]:
        segments = st.multiselect(
            "Segment",
            sorted(df["segment"].unique().tolist()),
            default=sorted(df["segment"].unique().tolist()),
        )
    with controls[2]:
        metric = st.radio("Ana metrik", ["gelir", "adet"], horizontal=True)

    filtered = df[(df["bölge"] == region) & (df["segment"].isin(segments))]
    if filtered.empty:
        st.warning("Seçim sonucu veri kalmadı.")
        return

    monthly = filtered.groupby("ay", as_index=False)[metric].sum()
    by_channel = filtered.groupby("kanal", as_index=False)[metric].sum()

    top = st.columns(3)
    top[0].metric("Toplam değer", f"{monthly[metric].sum():,.0f}")
    top[1].metric("Aylık ortalama", f"{monthly[metric].mean():,.1f}")
    top[2].metric("Segment sayısı", len(segments))

    trend = px.line(
        monthly,
        x="ay",
        y=metric,
        markers=True,
        title=f"{region} için aylık {metric} trendi",
        template="plotly_white",
    )
    trend.update_layout(hovermode="x unified", margin=dict(t=60, l=10, r=10, b=10))

    channel = px.bar(
        by_channel,
        x="kanal",
        y=metric,
        color="kanal",
        title=f"{region} için kanal bazlı {metric}",
        template="plotly_white",
        text_auto=True,
    )
    channel.update_layout(showlegend=False, margin=dict(t=60, l=10, r=10, b=10))

    left, right = st.columns([1.22, 0.92], gap="large")
    with left:
        st.plotly_chart(
            trend,
            use_container_width=True,
            theme=None,
            config={"displaylogo": False},
        )
        st.plotly_chart(
            channel,
            use_container_width=True,
            theme=None,
            config={"displaylogo": False},
        )
    with right:
        render_note_card(
            "Bu sekmede hangi fikri kapatın?",
            [
                "Widget değiştikçe grafik yeniden hesaplanıyorsa artık uygulama mantığı içindeyiz.",
                "Aynı figür farklı giriş durumlarına tepki veriyorsa, Plotly bir web bileşenine dönüşür.",
                "Bu mantık Dash'te Input -> callback -> Output akışıyla resmileşir.",
            ],
        )
        st.code(
            """@callback(
    Output("trend", "figure"),
    Input("region", "value"),
    Input("segment", "value"),
)
def update_trend(region, segment):
    filtered = source.query(...)
    return build_figure(filtered)""",
            language="python",
        )
        st.caption(
            "Dash resmi callback modeli de aynı fikre dayanır: bir bileşenin özelliği değişince başka bir bileşenin özelliği güncellenir."
        )


def main() -> None:
    configure_page()
    inject_css()
    render_hero()

    tabs = st.tabs(TAB_LABELS)
    with tabs[0]:
        render_tab_difference()
    with tabs[1]:
        render_tab_express()
    with tabs[2]:
        render_tab_architecture()
    with tabs[3]:
        render_tab_selection()
    with tabs[4]:
        render_tab_timeseries()
    with tabs[5]:
        render_tab_hierarchy()
    with tabs[6]:
        render_tab_dashboard()


if __name__ == "__main__":
    main()
