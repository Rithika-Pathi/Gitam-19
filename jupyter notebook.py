{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "90\n"
     ]
    }
   ],
   "source": [
    "def printEven(n):\n",
    "    cnt=0;\n",
    "    sum=0;\n",
    "    while(cnt!=n):\n",
    "        if(cnt%2==0):\n",
    "          sum=sum+cnt;\n",
    "        cnt=cnt+1;\n",
    "    return sum;  \n",
    "        \n",
    "print(printEven(20));        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 6 12 "
     ]
    }
   ],
   "source": [
    "def factorsList(n):\n",
    "    i=1;\n",
    "    while(1!=n):\n",
    "        if(n%i==0):\n",
    "            print(i,end=\" \");\n",
    "        i=i+1;\n",
    "    return;\n",
    "factorsList(12);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5, 6]\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "list=[1,2,3,4,5,6]\n",
    "print(list);\n",
    "print(list[0]);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Akhil Arvind Anil Akash "
     ]
    }
   ],
   "source": [
    "list=[\"Akhil\",\"Arvind\",\"Anil\",\"Akash\"];\n",
    "for x in list:\n",
    "    print(x,end=\" \");"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 6 7 \n",
      "5\n",
      "[4, 5, 6, 7]\n",
      "[1, 2, 3]\n",
      "[1, 2, 3, 4, 5, 6, 7]\n"
     ]
    }
   ],
   "source": [
    "list=[1,2,3,4,5,6,7]\n",
    "for x in list:\n",
    "    print(x,end=\" \");\n",
    "print();\n",
    "print(list[4]);\n",
    "print(list[3:7]);\n",
    "print(list[:3]);\n",
    "print(list[:7]);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1 2 3 4 5 6 7 8 9 10 \n",
      "[2, 3, 4, 5, 6, 7, 8, 9]\n",
      "[3, 4, 5, 6, 7, 8]\n",
      "[1, 3, 5, 7, 9]\n",
      "[1, 4, 7, 10]\n",
      "[1, 5, 9]\n",
      "[10, 8, 6, 4, 2]\n",
      "10\n",
      "9\n"
     ]
    }
   ],
   "source": [
    "list=[1,2,3,4,5,6,7,8,9,10]\n",
    "for x in list:\n",
    "    print(x,end=\" \")\n",
    "    \n",
    "print();\n",
    "print(list[1:-1]);\n",
    "print(list[2:-2]);\n",
    "print(list[::2]);\n",
    "print(list[::3]);\n",
    "print(list[::4]);\n",
    "print(list[::-2]);\n",
    "print(list[-1]);\n",
    "print(list[-2]);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['rithika', 'anvita', 'shruti', '1']\n",
      "['rithika', 'anvita', 15, '1']\n",
      "['rithika', 'anvita', 15]\n",
      "['rithika', 'gitam', 15]\n",
      "['rithika', 'gitam', 15, 1, 2, 3, 4, 5, 6]\n"
     ]
    }
   ],
   "source": [
    "list=[\"rithika\",\"anvita\",\"shruti\",\"1\"]\n",
    "print(list)\n",
    "list[2]=15\n",
    "print(list)\n",
    "del list[3]\n",
    "print(list)\n",
    "list[1]=\"gitam\"\n",
    "print(list)\n",
    "list1=[1,2,3,4,5,6]\n",
    "print(list+list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1, 2, 3, 4, 5]\n",
      "[1, 2, 4, 5]\n",
      "4\n",
      "[1, 2, 4, 5, 15, 150, 1, 3, 1]\n",
      "3\n",
      "1\n"
     ]
    }
   ],
   "source": [
    "list=[1,2,3,4,5]\n",
    "print(list)\n",
    "del list[2]\n",
    "print(list)\n",
    "print(len(list))\n",
    "list.append(15)\n",
    "list.append(150)\n",
    "list.append(1)\n",
    "list.append(3)\n",
    "list.append(1)\n",
    "print(list)\n",
    "print(list.count(1))\n",
    "print(list.count(3))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['rithika', 'anvita', 'shruti', '1']\n",
      "['rithika', 'anvita', 2019, 'shruti', '1']\n",
      "5\n",
      "['rithika', 'anvita', 2019, 'shruti', 2020, '1']\n"
     ]
    }
   ],
   "source": [
    "list=[\"rithika\",\"anvita\",\"shruti\",\"1\"]\n",
    "print(list)\n",
    "list.index(\"rithika\")\n",
    "list.index(\"1\")\n",
    "list.insert(2,2019)\n",
    "print(list)\n",
    "print(len(list))\n",
    "list.insert(4,2020)\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['rithika', 'anvita', 'shruti', 1, 'rithika', 'rithika', 'rithika', 'rithika']\n",
      "['anvita', 'shruti', 1, 'rithika', 'rithika', 'rithika', 'rithika']\n",
      "['anvita', 'shruti', 1, 'rithika', 'rithika', 'rithika']\n",
      "['anvita', 'shruti', 1, 'rithika', 'rithika']\n",
      "['anvita', 'shruti', 1, 'rithika']\n",
      "['rithika', 1, 'shruti', 'anvita']\n"
     ]
    }
   ],
   "source": [
    "list=[\"rithika\",\"anvita\",\"shruti\",1,\"rithika\",\"rithika\",\"rithika\",\"rithika\"]\n",
    "print(list)\n",
    "list.remove(\"rithika\")\n",
    "print(list)\n",
    "list.remove(\"rithika\")\n",
    "print(list)\n",
    "list.remove(\"rithika\")\n",
    "print(list)\n",
    "list.remove(\"rithika\")\n",
    "print(list)\n",
    "list.reverse()\n",
    "print(list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
