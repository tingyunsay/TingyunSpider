# -*- coding: utf-8 -*-
import random
import requests
from cookies import cookies


#微博专用cookies
class CookiesMiddleware(object):
		def process_request(self,request,spider):
				cookie = random.choice(cookies)
				request.cookies = eval(cookie)
			


"""
#测试cookies，打码之后返回的cookies格式，会有""空值，我已经在获取cookies的代码中将空置删除掉了，直接random选择一个然后eval即可得到需要的cookie
#				cookies = ['{"_T_WM": "a406eae00b8ae62ced12f8d43c220427", "gsid_CTandWM": "4uyC00841XqFbFIaZVjuqpaKQdo", "SUB": "_2A2513ysEDeRxGeNH4lsU9CrEyDyIHXVXI7VMrDV6PUJbkdANLUPnkW1nb72aQlMjScm30PNMRIaLPA4Vzg.."}', '{"_T_WM": "abc539d9436a047e01bf703656029be4", "gsid_CTandWM": "4u3T00841pn4sVpxRjkpEpaRze3", "SUB": "_2A2513ys1DeRhGeNH4lsY9i_EzD2IHXVXI7V9rDV6PUJbkdANLUXnkW1a-PBOPDA6LJelhcZqP6LVRvWvrw.."}', '{"_T_WM": "d65ee55912b4f074bf816600daad9e6c", "gsid_CTandWM": "4u2H00841a3upcEOxFN42paRzen", "SUB": "_2A2513yssDeRhGeNH4lsY9i_Ewj2IHXVXI7VkrDV6PUJbkdANLWbdkW1Q9SjwVXGvCq9amFeZHUT95tTxjg.."}', '{"_T_WM": "3505235e25fd47f2b33d0db12eda7dba", "gsid_CTandWM": "4uV200841Gk5qzdVciVxDpaKQeG", "SUB": "_2A2513yvdDeRxGeNH4lsU9CrFyjyIHXVXI7WVrDV6PUJbkdANLXLbkW1v6ZlnSzkwJpuKmjUkkQ3X0BJYxg.."}', '{"_T_WM": "50ea1066bba8fd4dc9c2f250f4f8217a", "gsid_CTandWM": "4uPK00841a6PLplzUpJJOpaXUfk", "SUB": "_2A2513yvMDeRxGeBO61IS9SrFzjyIHXVXI7WErDV6PUJbkdAKLWOhkW1DzUlEaxS02S8ySwW9kSBhSap8QQ.."}', '{"_T_WM": "1001a0dddeab99d730b1cb262975937e", "gsid_CTandWM": "4uOQ008419lpVWuO8jzQ8prrF3Z", "SUB": "_2A2513yuvDeRhGeBO7VEW8C3OzzuIHXVXI7XnrDV6PUJbkdAKLRfAkW2TnEiL8dfZFvDAL4HDO5Nv4xnAOw.."}']
"""

