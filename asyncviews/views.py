# Exercicio de processos assíncronos
import asyncio
from django.http import HttpResponse

async def process_data(data):
    await asyncio.sleep(2)  # Simulando um processo que leva algum tempo
    result = f"Processed data: {data}"
    print(result)

# itera de 1 a 5, aguardando 1 segundo entre cada iteração
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(f"Step {num} completed")
        await process_data(num)

# cria uma tarefa para executar a função http_call_async 
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse('Non-blocking HTTP request')