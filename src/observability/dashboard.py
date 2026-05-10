"""Observability dashboard for Agentic SDLC KPI metrics and system status."""

from __future__ import annotations

import sys
from datetime import datetime

try:
    import streamlit as st
    import plotly.graph_objects as go
    import plotly.express as px
except ImportError:
    print("Streamlit and Plotly not installed. Install with: pip install -e '.[ui]'")
    sys.exit(1)

from src.config import get_settings
from src.graphs.supervisor import get_kpi_tracker
from src.state.persistence import get_persistence_manager
from src.utils.logging import get_logger

logger = get_logger(__name__)


def setup_page():
    """Configure Streamlit page settings."""
    st.set_page_config(
        page_title="Agentic SDLC - Observability Dashboard",
        page_icon="📊",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.title("🚀 Agentic SDLC - Observability Dashboard")


def render_runtime_status():
    """Render runtime status section."""
    st.header("Runtime Status")

    settings = get_settings()
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Environment", settings.app_env)
    with col2:
        st.metric("HITL Enabled", "✓" if settings.enable_hitl else "✗")
    with col3:
        st.metric("Tracing Enabled", "✓" if settings.enable_tracing else "✗")
    with col4:
        st.metric("Log Level", settings.log_level)


def render_checkpoint_sessions():
    """Render checkpoint sessions section."""
    st.header("Checkpoint Sessions")

    manager = get_persistence_manager()
    sessions = manager.list_checkpoint_sessions()

    if sessions:
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"**Active Sessions**: {len(sessions)}")
        with col2:
            if st.button("🔄 Refresh"):
                st.rerun()

        with st.expander("Session List", expanded=len(sessions) <= 5):
            session_data = []
            for session_id in sessions:
                snapshot = manager.load_checkpoint_snapshot(session_id)
                session_data.append(
                    {
                        "Session ID": session_id,
                        "Phase": snapshot.get("phase", "unknown") if snapshot else "N/A",
                        "Updated": snapshot.get("metadata", {}).get("last_updated")
                        if snapshot
                        else "N/A",
                    }
                )
            st.dataframe(session_data, use_container_width=True)
    else:
        st.info("No checkpoint sessions found. Run a workflow to create one.")


def render_kpi_metrics():
    """Render KPI metrics section with visualizations."""
    st.header("Governance KPI Metrics")

    tracker = get_kpi_tracker()
    report = tracker.get_metrics_report()

    # Summary cards
    st.subheader("Summary")
    summary = report.get("summary", {})

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gate_pass_rate = summary.get("gate_pass_rate", "0.0%")
        st.metric("Gate Pass Rate", gate_pass_rate)
    with col2:
        first_attempt = summary.get("first_attempt_success_rate", "0.0%")
        st.metric("First Attempt Success", first_attempt)
    with col3:
        gates_attempted = summary.get("gates_attempted", 0)
        st.metric("Gates Attempted", gates_attempted)
    with col4:
        timestamp = report.get("timestamp", "N/A")
        st.metric("Last Updated", timestamp[-10:] if timestamp != "N/A" else "N/A")

    # Requirements traceability
    st.subheader("Requirements Traceability")
    requirements = report.get("requirements", {})
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Requirements", requirements.get("total", 0))
    with col2:
        st.metric("Verified", requirements.get("verified", 0))
    with col3:
        coverage = requirements.get("traceability_coverage", "0.0%")
        st.metric("Traceability Coverage", coverage)

    # Gate evidence completeness
    st.subheader("Gate Evidence Completeness")
    completeness = report.get("gate_evidence_completeness", {})
    if completeness:
        fig = go.Figure(
            data=[
                go.Bar(
                    x=list(completeness.keys()),
                    y=[
                        float(v.rstrip("%")) / 100
                        for v in completeness.values()
                    ],
                    marker_color="lightblue",
                )
            ]
        )
        fig.update_layout(
            title="Evidence Completeness by Gate",
            xaxis_title="Gate",
            yaxis_title="Completeness Score",
            yaxis=dict(range=[0, 1]),
            height=400,
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No gate evidence completeness data available yet.")

    # Agent contributions
    st.subheader("Agent Contributions")
    agents = report.get("agents", {})
    if agents:
        agent_data = [
            {"Agent": agent, "Contributions": count} for agent, count in agents.items()
        ]
        fig = px.bar(
            agent_data,
            x="Agent",
            y="Contributions",
            title="Agent Execution Count",
            height=400,
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("No agent contribution data available yet.")

    # Phase transition times
    phase_times = report.get("average_phase_transition_times", {})
    if phase_times:
        st.subheader("Phase Transition Times (Average)")
        phase_data = [
            {"Phase Transition": k, "Duration (seconds)": float(v.rstrip("s"))}
            for k, v in phase_times.items()
        ]
        fig = px.bar(
            phase_data,
            x="Phase Transition",
            y="Duration (seconds)",
            title="Average Phase Transition Duration",
            height=400,
        )
        st.plotly_chart(fig, use_container_width=True)

    # Agent execution times
    agent_times = report.get("average_agent_execution_times", {})
    if agent_times:
        st.subheader("Agent Execution Duration (Average)")
        agent_time_data = [
            {"Agent": agent, "Duration (seconds)": float(value.rstrip("s"))}
            for agent, value in agent_times.items()
        ]
        fig = px.bar(
            agent_time_data,
            x="Agent",
            y="Duration (seconds)",
            title="Average Agent Execution Duration",
            height=400,
        )
        st.plotly_chart(fig, use_container_width=True)


def render_historical_metrics():
    """Render historical health and event trend metrics."""
    st.header("Historical Metrics")

    manager = get_persistence_manager()
    health_events = manager.list_observability_events(event_type="health_snapshot")
    agent_events = manager.list_observability_events(event_type="agent_execution")

    if not health_events and not agent_events:
        st.info("No historical observability events found yet.")
        return

    if health_events:
        st.subheader("Health Check History")
        health_data = []
        for event in health_events:
            payload = event.get("payload", {})
            health_data.append(
                {
                    "Timestamp": event.get("created_at", ""),
                    "Overall Healthy": "yes"
                    if payload.get("all_healthy")
                    else "no",
                    "Docker": "ok" if payload.get("docker_ok") else "fail",
                    "Ollama": "ok" if payload.get("ollama_ok") else "fail",
                    "Postgres": "ok" if payload.get("postgres_ok") else "fail",
                    "Dependencies": "ok" if payload.get("deps_ok") else "fail",
                }
            )
        st.dataframe(health_data, use_container_width=True)

    if agent_events:
        st.subheader("Agent Execution Event History")
        event_data = []
        for event in agent_events:
            payload = event.get("payload", {})
            event_data.append(
                {
                    "Timestamp": event.get("created_at", ""),
                    "Agent": payload.get("agent", "unknown"),
                    "Duration (seconds)": payload.get("duration_seconds", 0.0),
                }
            )

        st.dataframe(event_data[:200], use_container_width=True)

        fig = px.line(
            event_data,
            x="Timestamp",
            y="Duration (seconds)",
            color="Agent",
            title="Agent Execution Duration Over Time",
            height=400,
        )
        st.plotly_chart(fig, use_container_width=True)


def render_about():
    """Render about section in sidebar."""
    with st.sidebar:
        st.header("About")
        st.write(
            """
        **Agentic SDLC AI** observability dashboard provides real-time visibility into:
        - Runtime configuration and status
        - Checkpoint session management
        - Governance KPI metrics
        - Gate completion and evidence quality
        - Agent execution patterns
        
        Use this dashboard to monitor system health and workflow progression.
        """
        )

        st.divider()

        st.write("**Version**: 0.1.0")
        st.write("**Status**: Active development")


def main():
    """Run the observability dashboard."""
    setup_page()
    render_about()

    tab1, tab2, tab3, tab4 = st.tabs(["Status", "Metrics", "Sessions", "History"])

    with tab1:
        render_runtime_status()

    with tab2:
        render_kpi_metrics()

    with tab3:
        render_checkpoint_sessions()

    with tab4:
        render_historical_metrics()


if __name__ == "__main__":
    main()
