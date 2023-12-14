README
2020035805
엄태곤 
보기 형태를 code로 보십시오(글자가 들쭉날쭉함)
과거 Object Detection 학습을 위해 공부했던 모든 내용을 여기에 적습니다.
누군가에겐 도움이 되길 바랍니다.
모든 사용예제는 여기 기재되어있습니다.
all usages are written below this line.
유전학습 구현 예제도 취미로 코딩해서 더해놨습니다.(주피터노트북)


#yolov8을이용한 오브젝트 디텍션 간단구현 및 파인튜닝 방법
<img width="477" alt="스크린샷 2023-12-14 오전 1 20 04" src="https://github.com/taegoneom/taegoneom.github.io/assets/99521902/73cde557-ef0b-421c-aaaf-5d44399e0357">




big help for implement from 
https://youtu.be/WgPbbWmnXJ8?si=05BeCO5x1BDJhsjf

image for yolo v8 custom/fine tuning from roboflow
https://universe.roboflow.com/sree-69ula/cats-and-dogs-hapzd/dataset/1

step by step guide
1. git 에서 다운로드 받아서 vscode에 작업 디렉토리로 열음
2. 원한다면 virtual env에서 실행 (venv env conda activate 등등 인터넷 찾아보면 있음)
3. 파이썬, 주피터노트북등 필요로하는 인터프리터랑 커널 설치
4. virtual env에서 실행하면 pip로 다운로드 받은 파일(ex. pip install -r requirements.txt) 을 거기서만 쓸수있어서 메인 파이썬이 손상안됨
5. yolov8 간단시연.py를 실행해보고 오류가 뜨면 오류가 뜬 패키지명을 pip로 받자. pip install ultralytics이런식으로
6. 실행하고 고양이가 잘 탐지되는지 확인.
7. 더 심화된 과정을 원하면 GCP에 클라우드컴퓨터를 하나 임대함(유료지만 처음사용하는 사람은 400달러 상당 무료 바우처 줌)
# 아래 과정을 진행할 사람은 이 구간 기준으로 역순으로 해야됩니다. 8.9.10 ~ 1.2.3
8. 임대한 컴퓨터에 remote로접속해서 cli로 cuda를 올바른 드라이버를 깔고 ,gcp 임대 컴퓨터 ip도 고정으로 할당받는다
9. NVIDIA T4 1대정도는 되야 2만장 이미지 정도는 반나절정도면 학습함(중간중간 실패하면(보통 gpu cunsumption이 꽉차고 해제가안되서 이슈가발생함. 그럴 시엔 취소하고 best.pt 찾아서 덮어씌워서 학습을 이어나가야함 그리고 gpu reset(클라우드컴퓨터를 재부팅하면 절대안된다)을 해주고 consumption 이 0 이 확인되면 이어서 한다.) 또한 학습시킬 이미지가 많다면 저장공간도 넉넉하게 잡으면 좋다.(부족하면 이미지 백업했다가 용량만 바꿔서 다시 임대신청해야한다)
10. 이제 환경구성이 완료되었다면 vscode에 kernal설정을 함. vscode 안에 ssh 를 통해 아까 할당받은 고정아이피, gcp 로그인 패스워드 등으로 gcp컴퓨터를 내집컴퓨터처럼 쓰면된다(연결 성공하면 새 창이뜨는데 거기서 ipynb랑 train images를 쓴다)
11. 필요한 파일은 scp 로 보내주고 받고 해줘야한다....(cats and dogs.zip , ipynb file, etc)
12. 사용자는 로컬pc에서 돌려놓고 에폭이 도는동안 다른작업을 하면된다.
13. 원하는 작업이 끝나지 않으면 gcp를 종료하지 않는것을 권고한다. 반납하면 다른 사람들이 gpu만 쏙 빼가서 본인 필요할때 부팅못할수있음(gpu 다른사람이 쓰고있어서)
14. 또한 400불 쓰기 직전이거나 pt파일이 원하는 accuracy에 도달해서 이제 그만해도 되면 gcp에 있는 백업이미지 포함 모든 데이터를 말소한다. 저장 자체로 과금이 된다.
15. 400불 바우처를 쓰려면 결제수단을 등록해야한다. 그렇기 때문에 한번 더 경고문을 적습니다.
16. 작업이 끝난 완성된 pt파일을 scp로 우리 컴퓨터로 전송해준다.
17. 1부터 7까지 다시 로컬에 셋업해서 간단시연.py에 적용하고 쓰면된다.

위가 싫으면 google colab으로 쓰거나 본인 컴퓨터를 NVIDIA T4급으로 구매하십시오

결과 그래프를 보면서 optimal depth? 
optimal epoch를 찾습니다.
data augmentation도 해보고
데이터 중간중간에 사이즈만 맞는 공백 이미지 도 10% 20% train data에 섞어보고..
hyperparameter 도 조정해보고..
overfit문제는 안 발생하는지 
gradient descent문제는 발생 안하는지
decay를 줘서 saturated neuron도 막아주고..

실제 .py파일에 넣어서 성능도 실험해봅니다.





