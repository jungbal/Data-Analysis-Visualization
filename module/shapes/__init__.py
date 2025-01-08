'''
기본적으로 패키지의 초기화 코드를 포함할 수 있습니다. 예를 들어, 패키지가 import 될 때 특정 변수를 설정하거나 다른 초기화 작업을 수행하려면 __init__.py 파일에 해당 코드를 작성합니다. 또한, __init__.py 파일을 사용하여 패키지 레벨에서의 import를 제어할 수 있습니다. 예를 들어, from shapes import *를 했을 때 어떤 모듈이 import 될지 정의할 수 있습니다. 아래 설정은 from shapes import *를 사용할 때 circle와 rectangle 모듈만 가져온다는 것을 의미합니다.
'''
__all__ = ['circle', 'rectangle']