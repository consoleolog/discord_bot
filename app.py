from dependency_injector import containers, providers

from service.ai_service import LLmService, AIService, DeepLService


class DiscordBotApplication(containers.DeclarativeContainer):
    config = providers.Configuration()

    llm_service = providers.Factory(LLmService)

    ai_service = providers.Factory(AIService)

    deepl_service = providers.Factory(DeepLService)
