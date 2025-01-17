'''
1. Fast API
FastAPI는 Python 기반의 웹 프레임워크로, 주로 API를 빠르게 개발하기 위해 설계되었습니다. FastAPI는 자동으로 생성되는 OpenAPI 문서(Swagger UI)를 통해 API의 사용성과 테스트를 쉽게 할 수 있으며, 데이터 유효성 검사와 타입 힌트를 활용한 코드 자동완성 및 오류 방지를 지원합니다. 특히, 비동기 처리를 활용하여 속도가 중요한 대규모 애플리케이션 개발에 적합하며, RESTful API와 GraphQL 같은 현대적 웹 API 개발에 유용합니다.
https://fastapi.tiangolo.com/ko/

※  타입 힌팅(Type Hints)
타입 힌팅(Type Hints)은 프로그래밍 언어에서 변수, 함수 매개변수, 함수 반환값 등에 대한 데이터 타입 정보를 코드에 명시적으로 제공하는 기술입니다. Python 3.5 이상에서 도입된 기능으로, 코드의 가독성을 높이고 프로그램의 안정성을 강화하는 데 도움이 됩니다.

FastApi
장점
FastAPI는 최신 Python 기반 프레임워크로 빠른 성능과 사용하기 쉬운 API로 유명합니다. 비동기 프로그래밍을 지원하므로 실시간 애플리케이션 구축에 적합합니다. 또한 자동 API 문서화 및 유효성 검사를 제공하여 개발자의 시간과 노력을 절약합니다.

단점
FastAPI는 비교적 새로운 프레임워크이며 기존 프레임워크에 비해 커뮤니티 지원 및 리소스가 많지 않을 수 있습니다. 또한 비동기 프로그래밍을 처음 접하는 개발자를 위한 학습 곡선도 있습니다.

활용도
FastAPI는 특히 데이터 집약적인 애플리케이션을 위한 실시간 및 고성능 API 구축에 적합합니다.

Django
장점
Django는 웹 애플리케이션 개발에 널리 사용되는 성숙한 Python 기반 프레임워크입니다. 인증, 관리자 패널 및 ORM과 같은 많은 기본 기능을 제공합니다. 또한 지원 및 리소스를 제공하는 크고 활동적인 커뮤니티가 있습니다.

단점
Django는 복잡할 수 있으며 설정하려면 상당한 구성이 필요합니다. 소규모 프로젝트나 경량 API 구축에는 적합하지 않을 수도 있습니다.

활용
Django는 웹 애플리케이션, 특히 콘텐츠 기반 웹사이트, 전자상거래 플랫폼 및 소셜 미디어 플랫폼을 구축하는 데 널리 사용됩니다.

Flask
장점
Flask는 배우고 사용하기 쉬운 경량 Python 기반 프레임워크입니다. 유연성을 제공하고 개발자가 모듈식 및 확장 가능한 방식으로 웹 애플리케이션을 구축할 수 있도록 합니다. 또한 사용자 정의가 가능하고 소규모 프로젝트를 구축하는 데 적합합니다.

단점
Flask는 다른 프레임워크에 비해 기본 제공 기능이 적기 때문에 개발자가 구현하는 데 더 많은 노력과 시간이 필요할 수 있습니다. 또한 대규모 웹 애플리케이션을 구축하는 데 적합하지 않을 수도 있습니다.

활용
Flask는 개인 웹 사이트, 간단한 API 및 내부 대시보드와 같은 소규모 웹 애플리케이션 및 프로토타입을 구축하는 데 적합합니다.

요약
FastAPI는 실시간 및 고성능 API를 구축하는 데 적합한 현대적이고 빠른 프레임워크이고, Django는 복잡한 웹 애플리케이션을 구축하는 데 적합한 성숙한 프레임워크이며, Flask는 소규모 웹 애플리케이션 및 프로토타입을 구축하는 데 적합한 가볍고 유연한 프레임워크입니다. . 그들 사이의 선택은 개발 팀의 기술과 경험뿐만 아니라 프로젝트의 특정 요구 사항과 요구 사항에 따라 다릅니다.
'''