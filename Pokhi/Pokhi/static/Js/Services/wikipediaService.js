﻿app.factory("wikipediaService", ["$http" , function ($http) {

    var _lastPageId = 0;
    var _feedEnded = false;
    var _getEndStubData = function(){
        return [{
            "content": ".....",
            "images": [
            ],
            "summary": "End of Feed. No more articles.",
            "title": "End of Feed. No more articles.",
            "topic": "End of Feed. No more articles.",
        }];
    };

    return {
        getPage: function (topic, callback) {

            callback({
                "data": {
                    "content": "page.content",
                    "images": [
                      "https://upload.wikimedia.org/wikipedia/commons/e/e9/Official_portrait_of_Barack_Obama.jpg",
                    ],
                    "summary": "Barack Hussein Obama II (US /bəˈrɑːk huːˈseɪn oʊˈbɑːmə/ bə-RAHK hoo-SAYN oh-BAH-mə; born August 4, 1961) is an American politician who served as the 44th President of the United States from 2009 to 2017. He is the first African American to have served as president, as well as the first born outside the contiguous United States. He previously served in the U.S. Senate representing Illinois from 2005 to 2008, and in the Illinois State Senate from 1997 to 2004. Obama was born in Honolulu, Hawaii, two years after the territory was admitted to the Union as the 50th state. He grew up mostly in Hawaii, but also spent one year of his childhood in Washington State and four years in Indonesia. After graduating from Columbia University in 1983, he worked as a community organizer in Chicago. In 1988 Obama enrolled in Harvard Law School, where he was the first black president of the Harvard Law Review. After graduation, he became a civil rights attorney and professor, teaching constitutional law at the University of Chicago Law School from 1992 to 2004. Obama represented the 13th District for three terms in the Illinois Senate from 1997 to 2004, when he ran for the U.S. Senate. Obama received national attention in 2004, with his unexpected March primary win, his well-received July Democratic National Convention keynote address, and his landslide November election to the Senate. In 2008, Obama was nominated for president, a year after his campaign began, and after a close primary campaign against Hillary Clinton. He was elected over Republican John McCain, and was inaugurated on January 20, 2009. Nine months later, Obama was named the 2009 Nobel Peace Prize laureate. During his first two years in office, Obama signed many landmark bills. Main reforms were the Patient Protection and Affordable Care Act (often referred to as 'Obamacare'), the Dodd–Frank Wall Street Reform and Consumer Protection Act, and the Don't Ask, Don't Tell Repeal Act of 2010. The American Recovery and Reinvestment Act of 2009 and Tax Relief, Unemployment Insurance Reauthorization, and Job Creation Act of 2010 served as economic stimulus amidst the Great Recession, but the GOP regained control of the House of Representatives in 2011. After a lengthy debate over the national debt limit, Obama signed the Budget Control and the American Taxpayer Relief Acts. In foreign policy, Obama increased U.S. troop levels in Afghanistan, reduced nuclear weapons with the U.S.-Russian New START treaty, and ended military involvement in the Iraq War. He ordered military involvement in Libya in opposition to Muammar Gaddafi, and the military operation that resulted in the death of Osama bin Laden. After winning re-election by defeating Republican nominee Mitt Romney, Obama was sworn in for a second term in 2013. During his second term, Obama promoted greater inclusiveness for LGBT Americans, with his administration filing briefs that urged the Supreme Court to strike down same-sex marriage bans as unconstitutional (United States v. Windsor and Obergefell v. Hodges). Obama also advocated gun control in response to the Sandy Hook Elementary School shooting, and issued wide-ranging executive actions concerning climate change and immigration. In foreign policy, Obama ordered military intervention in Iraq in response to gains made by ISIL after the 2011 withdrawal from Iraq, continued the process of ending U.S. combat operations in Afghanistan, promoted discussions that led to the 2015 Paris Agreement on global climate change, initiated the sanctions against Russia following the invasion in Ukraine, brokered a nuclear deal with Iran, and normalized U.S. relations with Cuba. Obama left office in January 2017 with a 60% approval rating. He currently resides in Washington, D.C. His presidential library will be built in Chicago.",
                    "title": "Barack Obama",
                    "topic": "barak obama",
                }
                }.data)
        },
        getEndStubData: _getEndStubData
        , getFeed: function (callback, count) {

            if (_feedEnded == true) {
                callback([]);
                return;
            }
            count = count || 10;

            $http({
                         url: "/api/wikipedia/feed",
                         data: { "count": count , "lastId" : _lastPageId },
                         method : 'POST'
                      })
                      .success(function (response) {
                          var feed = response.data.feed;
                          _lastPageId = response.data.lastId;
                          if (feed.length === 0) {
                              feed = _getEndStubData();
                              _feedEnded = true;
                          }
                          if (callback)
                              callback(feed);
                          
                      })
            
        }

    }
    
}])