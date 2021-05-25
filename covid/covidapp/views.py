from django.shortcuts import render

# Create your views here.
import requests
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "aea1db59ebmsh03731be902681a6p1b639djsndc64dc27f6ee",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()


def home(request):

    if request.method=='POST':
        selected_country= request.POST['selected_country']
        noofresults = int(response['results'])
        for  i in range(noofresults):
            if selected_country==response['response'][i]['country']:
                new=response['response'][i]['cases']['new']
                active=response['response'][i]['cases']['active']
                critical=response['response'][i]['cases']['critical']
                recovered=response['response'][i]['cases']['recovered']
                Total=response['response'][i]['cases']['total']
                deaths=int(Total)-int(active)-int(recovered)
        context={'selected_country':selected_country,'new':new,'active':active,'critical':critical,'recovered':recovered,'total':Total,'deaths':deaths}
        return render(request, 'home.html', context)
    noofresults= int(response['results'])
    list=[]
    for i in range(noofresults):
        list.append(response['response'][i]['country'])
    list=sorted(list)
    #context={'response':response['response'][0]}
    return render(request,'home.html', {'list':list})
