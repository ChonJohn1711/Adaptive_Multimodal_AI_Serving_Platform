class GatewayService:
    def __init__(self) -> None:
        self.name = 'gateway'

    def health(self) -> dict:
        return {'status': 'ok'}
