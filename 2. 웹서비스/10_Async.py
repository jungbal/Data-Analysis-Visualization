'''
1. 비동기 프로그래밍
비동기 프로그래밍은 코드가 병렬적으로 실행되는 것처럼 보이게 하는 프로그래밍 방식입니다. 이는 특히 I/O 작업(네트워크 요청, 파일 읽기/쓰기 등)에서 시간을 절약하고 프로그램의 성능을 최적화하는 데 유용합니다.

1) 동기(Synchronous)
작업이 순차적으로 실행됩니다. 하나의 작업이 끝날 때까지 다음 작업이 대기합니다.
'''
# # def 키워드로 선언하는 모든 함수는 파이썬에서 기본적으로 동기 방식으로 동작
# def do_sync():
#     print("do_sync")
#
# do_sync()

'''
2) 비동기(Asynchronous)
작업이 독립적으로 실행되며, 대기 시간이 발생하면 다른 작업을 처리할 수 있습니다.
'''
# def 키워드 앞에 async 키워드를 붙이면 함수는 비동기 처리됨
# 이러한 비동기 함수를 파이썬에서는 코루틴(coroutine)이라고 함
# async def do_async():
#     print("do_async")
# 비동기 함수는 일반 동기 함수가 호출하듯이 호출하면 coroutine 객체가 리턴
# do_async()

# import asyncio
#
# async def do_async():
#     print("do_async")
#
# # 비동기 함수는 일반적으로 async 로 선언된 다른 비동기 함수 내에서 await 키워드를 붙여서 호출해야 함
# # await 는 비동기 함수나 코루틴의 실행을 일시 중단하고 다른 작업을 처리할 수 있도록 함
# async def main_async():
#     await do_async()
#
# # async 로 선언되지 않은 일반 동기 함수 내에서 비동기 함수를 호출하려면 asyncio.run 을 이용
# asyncio.run(main_async())

'''
※ 코루틴(Coroutine)
파이썬에서 비동기 프로그래밍을 구현하기 위해 사용하는 특별한 형태의 함수입니다. 일반 함수와는 달리, 코루틴은 실행 중에 멈췄다가 다시 실행을 재개할 수 있습니다. 이를 통해 작업을 효율적으로 분할하고 비동기 처리를 가능하게 합니다.
'''

'''
1. 일반적인 메인 함수
메인 함수는 서브 루틴을 호출한 뒤 서브 루틴의 작업이 끝날 때까지 기다립니다. 만약 서브 루틴이 파일 I/O 내지 대용량 파일 다운로드와 같은 작업을 수행한다면 서브 루틴이 작업을 마칠 때까지 기다려야 합니다.

2. 코루틴
코루틴은 함수가 종료되지 않은 상태에서 메인 루틴의 코드를 실행한 뒤 다시 돌아와서 코루틴의 코드를 실행합니다. 따라서 코루틴이 종료되지 않았으므로 코루틴의 내용도 계속 유지됩니다. 일반 함수를 호출하면 코드를 한 번만 실행할 수 있지만, 코루틴은 코드를 여러 번 실행할 수 있습니다.
'''

import asyncio

async def task(name, duration):
    print(f"{name} 시작")
    await asyncio.sleep(duration)
    print(f"{name} 완료")

async def main():
    await asyncio.gather(
        task("작업 1", 2),
        task("작업 2", 3),
        task("작업 3", 1)
    )

asyncio.run(main())

'''
2. 비동기 프로그래밍을 사용하는 이유

1) 응답성(Responsiveness): 비동기 작업은 여러 작업을 동시에 처리하고, 작업이 완료되기를 기다리는 동안 다른 작업을 처리할 수 있습니다. 이로써 프로그램의 응답성이 향상되고, 장기 실행 작업이 다른 작업을 차단하지 않도록 할 수 있습니다. 예를 들어, 네트워크 요청이나 데이터베이스 조회 등의 I/O 작업을 비동기로 처리하면, 다른 작업을 수행하면서 응답을 기다릴 필요가 없어집니다.

2) 확장성(Scalability): 비동기 프로그래밍은 많은 수의 동시 요청 또는 작업을 처리할 때 유용합니다. 여러 작업을 동시에 실행하고 완료될 때까지 기다리지 않아도 되므로, 처리량과 처리 속도를 향상시킬 수 있습니다. 이는 웹 서버, 네트워크 서비스, 데이터 파이프라인 등과 같은 시스템의 확장성을 향상시키는 데 도움이 됩니다.

3) 자원 효율성(Resource Efficiency): 비동기 작업은 작업의 대기 시간 동안 자원을 효율적으로 활용할 수 있습니다. 대기 시간 동안 CPU나 메모리 등의 자원을 다른 작업에 할당하여 더 많은 작업을 처리할 수 있습니다. 이는 시스템의 자원 이용률을 높이고, 전체적인 성능을 향상시킬 수 있습니다.

4) 병렬성(Concurrency): 비동기 프로그래밍은 병렬적인 작업을 효율적으로 처리할 수 있는 방법을 제공합니다. 여러 작업이 동시에 실행될 수 있으며, 이는 멀티코어 프로세서를 활용하여 작업을 분산 처리할 수 있음을 의미합니다. 이를 통해 병렬성을 높여 전체적인 처리 시간을 단축시킬 수 있습니다.
'''