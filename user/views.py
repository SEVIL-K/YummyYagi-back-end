from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from story.models import Story
from user.serializers import UserSerializer, LoginSerializer, MypageSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class RegisterView(APIView):
    """사용자 정보를 받아 회원가입 합니다."""
    def post(self, request):
        if request.data['password'] != request.data['password_check']:
            return Response({'status':'400', 'error':'비밀번호를 확인해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'status':'201', 'success':'회원가입 성공'}, status=status.HTTP_201_CREATED)
            return Response({'status':'400', 'error':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(TokenObtainPairView):
    """
    사용자 정보를 받아 로그인 합니다.
    
    DRF의 JWT 토큰 인증 로그인 방식에 기본 제공되는 클래스 뷰를 상속받아 재정의합니다.
    """
    serializer_class = LoginSerializer


class MyPageView(APIView):
    """사용자의 마이페이지입니다."""
    def get(self, request):
        user = request.user
        serializer = MypageSerializer(user)
        return Response({'status':'200', 'my_data':serializer.data}, status=status.HTTP_200_OK)


class UserInfoView(APIView):
    def get(self, request):
        """사용자의 회원 정보 수정 페이지입니다."""
        pass
    
    def put(self, request):
        """사용자의 정보를 받아 회원 정보를 수정합니다."""
        pass
    
    def patch(self, request):
        """사용자의 정보를 받아 비밀번호를 수정합니다."""
        pass
    
    def delete(self, request):
        """사용자의 회원 탈퇴 기능입니다."""
        pass

    
class QnaView(APIView):
    def get(self, request):
        """Q&A 페이지입니다."""
        pass
    
    def post(self, request):
        """Q&A를 작성합니다."""
        pass