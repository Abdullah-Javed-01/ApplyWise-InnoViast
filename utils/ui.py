from html import escape
from typing import Callable

import streamlit as st


def inject_custom_css() -> None:
    """Apply the custom ApplyWise AI visual theme."""

    st.markdown(
        """
        <style>
        :root {
            --aw-bg: #080d17;
            --aw-panel: #0d1421;
            --aw-panel-soft: #111a29;
            --aw-border: rgba(148, 163, 184, 0.22);
            --aw-text: #f8fafc;
            --aw-muted: #94a3b8;
            --aw-pink: #ff416c;
            --aw-green: #35d07f;
            --aw-red: #ff5263;
            --aw-blue: #4da3ff;
            --aw-purple: #9d6cff;
        }

        .stApp {
            background:
                radial-gradient(
                    circle at top right,
                    rgba(37, 99, 235, 0.10),
                    transparent 34%
                ),
                var(--aw-bg);
        }

        .block-container {
            max-width: 1500px;
            padding-top: 2.6rem;
            padding-bottom: 4rem;
        }

        [data-testid="stHeader"] {
            background: rgba(8, 13, 23, 0.94);
            backdrop-filter: blur(12px);
        }

        html,
        body,
        p,
        li,
        label {
            font-size: 17px !important;
            line-height: 1.55 !important;
        }

        h1 {
            font-size: 2.65rem !important;
            font-weight: 850 !important;
            letter-spacing: -0.04em;
        }

        h2 {
            font-size: 1.55rem !important;
            font-weight: 800 !important;
        }

        h3 {
            font-size: 1.18rem !important;
            font-weight: 750 !important;
        }

        .aw-topbar {
            min-height: 52px;
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.9rem;
            margin-bottom: 1rem;
        }

        .aw-logo {
            font-size: 2.1rem;
        }

        .aw-brand {
            font-size: 1.75rem;
            font-weight: 850;
            color: var(--aw-text);
        }

        .aw-badge {
            display: inline-flex;
            align-items: center;
            padding: 0.35rem 0.75rem;
            border: 1px solid rgba(255, 65, 108, 0.42);
            border-radius: 999px;
            color: #ff7b9b;
            background: rgba(255, 65, 108, 0.08);
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.06em;
        }

        .aw-hero {
            padding: 1.8rem 2rem;
            margin-bottom: 1rem;
            border: 1px solid var(--aw-border);
            border-radius: 15px;
            background:
                linear-gradient(
                    115deg,
                    rgba(90, 25, 42, 0.52),
                    rgba(15, 23, 42, 0.95) 56%,
                    rgba(17, 54, 101, 0.58)
                );
            box-shadow: 0 18px 48px rgba(0, 0, 0, 0.22);
        }

        .aw-hero h1 {
            font-size: 1.75rem !important;
            margin: 0 0 0.6rem 0 !important;
        }

        .aw-hero p {
            max-width: 820px;
            color: #cbd5e1;
            margin-bottom: 0.8rem;
        }

        .aw-notice {
            display: inline-block;
            padding: 0.7rem 0.9rem;
            border-radius: 8px;
            background: rgba(30, 41, 59, 0.70);
            color: #dbeafe;
            font-size: 0.92rem;
        }

        .aw-panel {
            border: 1px solid var(--aw-border);
            border-radius: 13px;
            background:
                linear-gradient(
                    145deg,
                    rgba(17, 24, 39, 0.96),
                    rgba(9, 15, 27, 0.96)
                );
            padding: 1rem 1.1rem;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.17);
            margin-bottom: 0.8rem;
        }

        .aw-panel-title {
            font-size: 1.05rem;
            font-weight: 800;
            color: var(--aw-text);
            margin-bottom: 0.8rem;
        }

        .aw-success {
            padding: 0.7rem 0.9rem;
            border-radius: 9px;
            border: 1px solid rgba(53, 208, 127, 0.22);
            background: rgba(53, 208, 127, 0.09);
            color: #65e6a1;
            font-weight: 650;
            margin-bottom: 0.8rem;
        }

        .aw-summary-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.8rem;
        }

        .aw-stat-card {
            min-height: 118px;
            padding: 1rem;
            border-radius: 11px;
            border: 1px solid var(--aw-border);
            background: rgba(15, 23, 42, 0.82);
        }

        .aw-stat-label {
            font-size: 0.82rem;
            font-weight: 750;
            color: #cbd5e1;
        }

        .aw-stat-value {
            margin-top: 0.35rem;
            font-size: 1.75rem;
            font-weight: 900;
        }

        .aw-stat-help {
            margin-top: 0.25rem;
            font-size: 0.78rem;
            color: var(--aw-muted);
        }

        .aw-pink {
            color: var(--aw-pink);
        }

        .aw-green {
            color: var(--aw-green);
        }

        .aw-red {
            color: var(--aw-red);
        }

        .aw-skill-wrap {
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
        }

        .aw-skill {
            display: inline-block;
            padding: 0.32rem 0.65rem;
            border-radius: 7px;
            font-size: 0.83rem;
            font-weight: 600;
        }

        .aw-skill-matched {
            color: #70e7a7;
            border: 1px solid rgba(53, 208, 127, 0.42);
            background: rgba(53, 208, 127, 0.06);
        }

        .aw-skill-missing {
            color: #ff8b98;
            border: 1px solid rgba(255, 82, 99, 0.45);
            background: rgba(255, 82, 99, 0.06);
        }

        .aw-tag {
            display: inline-block;
            padding: 0.32rem 0.65rem;
            margin: 0.18rem;
            border-radius: 7px;
            border: 1px solid rgba(77, 163, 255, 0.40);
            background: rgba(77, 163, 255, 0.06);
            color: #a9d3ff;
            font-size: 0.82rem;
        }

        .aw-list {
            margin: 0;
            padding-left: 1.1rem;
            color: #d7e0ed;
        }

        .aw-list li {
            margin-bottom: 0.45rem;
            font-size: 0.88rem !important;
            overflow-wrap: anywhere;
        }

        .aw-empty {
            color: var(--aw-muted);
            font-size: 0.88rem;
        }

        .aw-empty-state {
            min-height: 460px;
        }

        .aw-empty-state-content {
            min-height: 350px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            gap: 0.7rem;
            text-align: center;
        }

        .aw-empty-state-icon {
            font-size: 3rem;
            opacity: 0.85;
        }

        .aw-empty-state-heading {
            font-size: 1.15rem;
            font-weight: 750;
            color: var(--aw-text);
        }

        .aw-comparison-card {
            height: 100%;
        }

        .aw-comparison-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 0;
            margin-top: 0.8rem;
        }

        .aw-comparison-side {
            min-width: 0;
            padding: 0.25rem 1rem 0.25rem 0;
        }

        .aw-comparison-side + .aw-comparison-side {
            padding-left: 1rem;
            padding-right: 0;
            border-left: 1px solid var(--aw-border);
        }

        .aw-comparison-content {
            margin-top: 0.7rem;
        }

        [data-testid="stFileUploader"] section {
            border-radius: 11px !important;
            border: 1px dashed rgba(148, 163, 184, 0.45) !important;
            min-height: 132px;
            background: rgba(15, 23, 42, 0.55);
        }

        textarea {
            border-radius: 10px !important;
            background: rgba(30, 41, 59, 0.64) !important;
            font-size: 0.96rem !important;
            line-height: 1.55 !important;
        }

        .stButton > button,
        [data-testid="stFormSubmitButton"] > button {
            min-height: 3rem;
            width: 100%;
            border-radius: 9px !important;
            border: 0 !important;
            background:
                linear-gradient(
                    90deg,
                    #df2860,
                    #ff4d61
                ) !important;
            color: white !important;
            font-weight: 800 !important;
        }

        [data-testid="stVerticalBlockBorderWrapper"] {
            border-color: var(--aw-border) !important;
            border-radius: 13px !important;
            background: rgba(9, 15, 27, 0.55);
        }

        [data-testid="stForm"] {
            border-color: var(--aw-border) !important;
            border-radius: 13px !important;
            background: rgba(9, 15, 27, 0.72);
        }

        div[role="radiogroup"] {
            gap: 0.45rem;
        }

        div[role="radiogroup"] label {
            border: 1px solid var(--aw-border);
            border-radius: 8px;
            padding: 0.5rem 0.75rem !important;
            background: rgba(15, 23, 42, 0.75);
        }

        @media (max-width: 1100px) {
            .aw-summary-grid {
                grid-template-columns: 1fr;
            }

            .aw-comparison-grid {
                grid-template-columns: 1fr;
            }

            .aw-comparison-side + .aw-comparison-side {
                margin-top: 1rem;
                padding-top: 1rem;
                padding-left: 0;
                border-left: 0;
                border-top: 1px solid var(--aw-border);
            }
        }

        @media (max-width: 900px) {
            .block-container {
                padding-left: 0.9rem;
                padding-right: 0.9rem;
            }

            .aw-hero {
                padding: 1.3rem;
            }

            .aw-brand {
                font-size: 1.45rem;
            }

            .aw-hero h1 {
                font-size: 1.45rem !important;
            }
        }
        
        @media (max-width: 1200px) {
            [data-testid="stHorizontalBlock"] {
                flex-direction: column !important;
            }

            [data-testid="stHorizontalBlock"] > div {
                width: 100% !important;
                flex: 1 1 100% !important;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def display_brand_header() -> None:
    """Display the ApplyWise AI header and introduction."""

    html = """
    <div class="aw-topbar">
        <div class="aw-logo">🎯</div>
        <div class="aw-brand">ApplyWise AI</div>
        <div class="aw-badge">AI-POWERED JOB MATCHING</div>
    </div>

    <div class="aw-hero">
        <h1>Understand how well your résumé matches a job</h1>

        <p>
            Upload your résumé and paste a job description to compare
            technical skills, experience, education, and role requirements.
        </p>

        <div class="aw-notice">
            Results are estimated from the information found in your
            résumé and the provided job description.
        </div>
    </div>
    """

    st.html(html)


def display_empty_state() -> None:
    """Display the result-panel placeholder before analysis."""

    html = """
    <div class="aw-panel aw-empty-state">
        <div class="aw-panel-title">
            📊 Your analysis will appear here
        </div>

        <div class="aw-empty-state-content">
            <div class="aw-empty-state-icon">📄</div>

            <div class="aw-empty-state-heading">
                Ready to compare your résumé
            </div>

            <div class="aw-empty">
                Upload your résumé, paste a job description,
                and select Analyze Match.
            </div>
        </div>
    </div>
    """

    st.html(html)


def display_success_message() -> None:
    """Display the completed-analysis message."""

    st.html(
        """
        <div class="aw-success">
            ✓ Analysis completed successfully.
        </div>
        """
    )


def display_summary_cards(
    score: float,
    matched_count: int,
    missing_count: int,
) -> None:
    """Display the technical score and skill totals."""

    html = f"""
    <div class="aw-panel">
        <div class="aw-panel-title">💡 Analysis Summary</div>

        <div class="aw-summary-grid">
            <div class="aw-stat-card">
                <div class="aw-stat-label">Skill Match</div>

                <div class="aw-stat-value aw-pink">
                    {score:.1f}%
                </div>

                <div class="aw-stat-help">
                    Technical skill match score
                </div>
            </div>

            <div class="aw-stat-card">
                <div class="aw-stat-label">Matched Skills</div>

                <div class="aw-stat-value aw-green">
                    {matched_count}
                </div>

                <div class="aw-stat-help">
                    Skills found in your résumé
                </div>
            </div>

            <div class="aw-stat-card">
                <div class="aw-stat-label">Missing Skills</div>

                <div class="aw-stat-value aw-red">
                    {missing_count}
                </div>

                <div class="aw-stat-help">
                    Skills not identified
                </div>
            </div>
        </div>
    </div>
    """

    st.html(html)


def display_skill_tags(
    title: str,
    skills: list[str],
    matched: bool,
) -> None:
    """Display matched or missing skills as compact tags."""

    skill_class = (
        "aw-skill-matched"
        if matched
        else "aw-skill-missing"
    )

    icon = "✅" if matched else "❌"
    count_label = "matched" if matched else "missing"

    if skills:
        skill_html = "".join(
            (
                f'<span class="aw-skill {skill_class}">'
                f"{escape(str(skill))}"
                "</span>"
            )
            for skill in sorted(
                skills,
                key=lambda value: str(value).lower(),
            )
        )
    else:
        skill_html = (
            '<span class="aw-empty">'
            "No skills identified."
            "</span>"
        )

    html = f"""
    <div class="aw-panel">
        <div class="aw-panel-title">
            {icon} {escape(title)}
        </div>

        <div class="aw-skill-wrap">
            {skill_html}
        </div>

        <div class="aw-stat-help" style="margin-top: 0.75rem;">
            {len(skills)} {count_label} skills
        </div>
    </div>
    """

    st.html(html)


def _list_html(items: list[str]) -> str:
    """Convert a list of text items into safe HTML."""

    if not items:
        return (
            '<div class="aw-empty">'
            "No information identified."
            "</div>"
        )

    list_items = "".join(
        f"<li>{escape(str(item))}</li>"
        for item in items
    )

    return f'<ul class="aw-list">{list_items}</ul>'


def display_comparison_card(
    title: str,
    icon: str,
    candidate_label: str,
    candidate_items: list[str],
    required_label: str,
    required_items: list[str],
) -> None:
    """Display candidate and job requirements side by side."""

    candidate_html = _list_html(candidate_items)
    required_html = _list_html(required_items)

    html = f"""
    <div class="aw-panel aw-comparison-card">
        <div class="aw-panel-title">
            {escape(icon)} {escape(title)}
        </div>

        <div class="aw-comparison-grid">
            <div class="aw-comparison-side">
                <div class="aw-stat-label">
                    {escape(candidate_label)}
                </div>

                <div class="aw-comparison-content">
                    {candidate_html}
                </div>
            </div>

            <div class="aw-comparison-side">
                <div class="aw-stat-label">
                    {escape(required_label)}
                </div>

                <div class="aw-comparison-content">
                    {required_html}
                </div>
            </div>
        </div>
    </div>
    """

    st.html(html)


def display_domain_tags(
    domain_items: list[str],
) -> None:
    """Display job-domain information as compact tags."""

    if not domain_items:
        return

    tags = "".join(
        (
            '<span class="aw-tag">'
            f"{escape(str(item))}"
            "</span>"
        )
        for item in domain_items
    )

    html = f"""
    <div class="aw-panel">
        <div class="aw-panel-title">
            🧭 Domain Knowledge Mentioned
        </div>

        <div>
            {tags}
        </div>
    </div>
    """

    st.html(html)


@st.fragment
def display_feedback_form(
    job_title: str,
    technical_skill_score: float,
    save_feedback_function: Callable,
) -> None:
    """Display and process the anonymous feedback form."""

    st.html(
        """
        <div class="aw-panel">
            <div class="aw-panel-title">
                ⭐ Share Your Feedback
            </div>

            <div class="aw-stat-help">
                Help us improve ApplyWise AI for future users.
            </div>
        </div>
        """
    )

    with st.popover(
        "Share Feedback",
        use_container_width=True,
    ):
        with st.form(
            "applywise_feedback_form",
            clear_on_submit=True,
        ):
            rating = st.radio(
                "Overall experience",
                options=[1, 2, 3, 4, 5],
                index=3,
                horizontal=True,
                format_func=lambda value: f"{value} ⭐",
            )

            feedback_text = st.text_area(
                "Anything you'd like to share? (Optional)",
                placeholder=(
                    "Tell us what was helpful, inaccurate, "
                    "or not working properly."
                ),
                height=120,
            )

            submitted = st.form_submit_button(
                "Submit Feedback",
                use_container_width=True,
            )

        if submitted:
            with st.spinner("Submitting feedback..."):
                success, message = save_feedback_function(
                    rating=rating,
                    feedback_text=feedback_text,
                    job_title=job_title,
                    technical_skill_score=technical_skill_score,
                )

            if success:
                st.success(message)
            else:
                st.error(message)