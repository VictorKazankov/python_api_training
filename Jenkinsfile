node {
    stage("Checkout repo"){
        git branch: '2-th_version_framework',
        url: 'https://github.com/VictorKazankov/python_api_training'
    }
    stage("Install deps"){
        bat 'pipenv install'
    }
    stage("Test"){
        bat 'pipenv run pytest tests -sv --alluredir=allure_results'
    }
}