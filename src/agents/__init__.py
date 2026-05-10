"""Agent implementations for the Agentic SDLC system."""

from src.agents.architecture_agent import ArchitectureAgent
from src.agents.base_agent import BaseAgent
from src.agents.data_management_agent import DataManagementAgentStub
from src.agents.chief_compliance_officer import ChiefComplianceOfficerAgent
from src.agents.integration_and_test_agent import IntegrationAndTestAgentStub
from src.agents.chief_engineer import ChiefEngineerAgent
from src.agents.chief_reliability_officer import ChiefReliabilityOfficerAgent
from src.agents.chief_safety_officer import ChiefSafetyOfficerAgent
from src.agents.chief_security_officer import ChiefSecurityOfficerAgent
from src.agents.configuration_management_agent import ConfigurationManagementAgent
from src.agents.cyber_architect import CyberArchitectAgent
from src.agents.integration_manager import IntegrationManagerAgent
from src.agents.operations_lead import OperationsLeadAgent
from src.agents.program_manager import ProgramManagerAgent
from src.agents.qa_manager import QAManagerAgent
from src.agents.requirements_agent import RequirementsAgent
from src.agents.software_development_agent import SoftwareDevelopmentAgent
from src.agents.software_quality_manager import SoftwareQualityManagerAgent
from src.agents.verification_validation_agent import VerificationValidationAgent

__all__ = [
    "ArchitectureAgent",
    "BaseAgent",
    "DataManagementAgentStub",
    "ChiefComplianceOfficerAgent",
    "IntegrationAndTestAgentStub",
    "ChiefEngineerAgent",
    "ChiefReliabilityOfficerAgent",
    "ChiefSafetyOfficerAgent",
    "ChiefSecurityOfficerAgent",
    "ConfigurationManagementAgent",
    "CyberArchitectAgent",
    "IntegrationManagerAgent",
    "OperationsLeadAgent",
    "ProgramManagerAgent",
    "QAManagerAgent",
    "RequirementsAgent",
    "SoftwareDevelopmentAgent",
    "SoftwareQualityManagerAgent",
    "VerificationValidationAgent",
]