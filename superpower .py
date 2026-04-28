{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNFW+BoA5Hc7kno9IgWLgGt",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Ashraf-Dev-stack/python-game-superhero/blob/main/superpower%20.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ScLnkIOfUdqZ",
        "outputId": "518b0edf-abbc-4294-c55d-261eb0115ce8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Choose a superpower :)\n",
            "1- Flying\n",
            "2- Invisibility\n",
            "3- Super Speed\n",
            "Enter the number: 1\n",
            "Now :You can fly in the sky like a superhero !!\n"
          ]
        }
      ],
      "source": [
        "import sys\n",
        "import time\n",
        "\n",
        "def slow_print(text, delay=0.05):\n",
        "    for char in text:\n",
        "        sys.stdout.write(char)\n",
        "        sys.stdout.flush()\n",
        "        time.sleep(delay)\n",
        "    sys.stdout.write('\\n')\n",
        "    sys.stdout.flush()\n",
        "\n",
        "slow_print(\"Choose a superpower :)\")\n",
        "slow_print(\"1- Flying\")\n",
        "slow_print(\"2- Invisibility\")\n",
        "slow_print(\"3- Super Speed\")\n",
        "\n",
        "choice = input(\"Enter the number: \")\n",
        "\n",
        "if choice == \"1\":\n",
        "    slow_print(\"Now :You can fly in the sky like a superhero !!\")\n",
        "elif choice == \"2\":\n",
        "    slow_print(\"Now :You became invisible, no one can see you !!\")\n",
        "elif choice == \"3\":\n",
        "    slow_print(\"Now :You are as fast as lightning !!\")\n",
        "else:\n",
        "    slow_print(\"Invalid choice ?\")\n",
        ""
      ]
    }
  ]
}