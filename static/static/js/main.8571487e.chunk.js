(this.webpackJsonpviewer=this.webpackJsonpviewer||[]).push([[0],{447:function(e,t,a){e.exports=a(938)},452:function(e,t,a){},454:function(e,t,a){},476:function(e,t){},478:function(e,t){},510:function(e,t){},511:function(e,t){},576:function(e,t){},671:function(e,t,a){},938:function(e,t,a){"use strict";a.r(t);var n=a(1),r=a.n(n),l=a(9),o=a.n(l),c=(a(452),a(113)),m=a.n(c),i=a(179),u=a(116),s=a(13),d=a.n(s),p=(a(454),a(397)),E=a.n(p),h=window.origin,f={run_simulation:function(){var e=Object(i.a)(m.a.mark((function e(t){return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,e.next=3,E.a.post("".concat(h,"/api/predict"),{body:t,json:!0});case 3:return e.abrupt("return",e.sent);case 6:return e.prev=6,e.t0=e.catch(0),e.abrupt("return",void 0);case 9:case"end":return e.stop()}}),e,null,[[0,6]])})));return function(t){return e.apply(this,arguments)}}()},g=a(398),y=(a(671),a(946)),b=a(942),v=a(117),O=a(54),w=a(944),T=a(939),C=a(417),j=a(943),x=a(418);function k(e,t){var a=Object.keys(e);if(Object.getOwnPropertySymbols){var n=Object.getOwnPropertySymbols(e);t&&(n=n.filter((function(t){return Object.getOwnPropertyDescriptor(e,t).enumerable}))),a.push.apply(a,n)}return a}function D(e){for(var t=1;t<arguments.length;t++){var a=null!=arguments[t]?arguments[t]:{};t%2?k(a,!0).forEach((function(t){Object(g.a)(e,t,a[t])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(a)):k(a).forEach((function(t){Object.defineProperty(e,t,Object.getOwnPropertyDescriptor(a,t))}))}return e}var I={target:22,output:1e3,roomX:8,roomY:10,roomZ:2.75,window:4,interval:20,fromDate:d()().startOf("day").add(1,"d"),fromTime:d()().startOf("day").add(20,"h"),toDate:d()().startOf("day").add(2,"d"),toTime:d()().startOf("day").add(8,"h"),location:"Hamilton"},W=function(e){var t=e.onCalculate,a=e.disabled,l=Object(n.useState)(I),o=Object(u.a)(l,2),c=o[0],m=o[1],i=Object(n.useCallback)((function(){t&&t(function(e){var t=[e.fromTime.clone(),e.fromDate.clone(),e.toTime.clone(),e.toDate.clone()],a=t[1],n=t[2],r=t[3],l=t[0].set({year:a.year(),month:a.month(),date:a.date()}).unix(),o=n.set({year:r.year(),month:r.month(),date:r.date()}).unix();return{A:{ROOF:e.roomX*e.roomY,WALL:2*e.roomX+2*e.roomY-e.window,FLOOR:e.roomX*e.roomY,WINDOW_SINGLE_WOOD:e.window},volume:e.roomX*e.roomY*e.roomZ,interval:e.interval,target_temp:e.target,location:e.location,heater:e.output,from:l,to:o}}(c))}),[t,c]),s=function(e){return function(t){var a=D({},c);a[e]=t||0,m(a)}},d=function(e){return function(t){if(t){var a=D({},c);a[e]=t,m(a)}}};return r.a.createElement(y.a,{style:{maxWidth:"650px"}},r.a.createElement(b.a,{className:"ConfigForm",layout:"vertical"},r.a.createElement(v.a,{gutter:6},r.a.createElement(O.a,{span:12},r.a.createElement(b.a.Item,{label:"Target Temperature (\xb0C)"},r.a.createElement(w.a,{onChange:s("target"),style:{width:"100%"},value:c.target,placeholder:"0 \xb0C"}))),r.a.createElement(O.a,{span:12},r.a.createElement(b.a.Item,{label:"Heater Output (W)"},r.a.createElement(w.a,{onChange:s("output"),style:{width:"100%"},value:c.output,placeholder:"0 W"})))),r.a.createElement(v.a,{gutter:6},r.a.createElement(O.a,{span:10},r.a.createElement(b.a.Item,{label:"Room Dimensions (m)"},r.a.createElement(v.a,{gutter:3},r.a.createElement(O.a,{span:11},r.a.createElement(w.a,{onChange:s("roomX"),style:{width:"100%"},value:c.roomX,placeholder:"0 m"})),r.a.createElement(O.a,{span:2,style:{paddingTop:3}},"x"),r.a.createElement(O.a,{span:11},r.a.createElement(w.a,{onChange:s("roomY"),style:{width:"100%"},value:c.roomY,placeholder:"0 m"}))))),r.a.createElement(O.a,{span:7},r.a.createElement(b.a.Item,{label:"Ceiling Height (m)"},r.a.createElement(w.a,{onChange:s("roomZ"),style:{width:"100%"},value:c.roomZ,placeholder:"0 m"}))),r.a.createElement(O.a,{span:7},r.a.createElement(b.a.Item,{label:"Window Area (m\xb2)"},r.a.createElement(w.a,{onChange:s("window"),style:{width:"100%"},value:c.window,placeholder:"0 m\xb2"})))),r.a.createElement(v.a,{gutter:6},r.a.createElement(O.a,{span:24},r.a.createElement(b.a.Item,{label:"Time Range"},r.a.createElement(v.a,{gutter:3},r.a.createElement(O.a,{span:5},r.a.createElement(T.a,{onChange:d("fromDate"),defaultValue:c.fromDate})),r.a.createElement(O.a,{span:6},r.a.createElement(C.a,{onChange:d("fromTime"),defaultValue:c.fromTime,format:"h:mm a",use12Hours:!0})),r.a.createElement(O.a,{span:2,style:{paddingTop:3,textAlign:"center"}},"to"),r.a.createElement(O.a,{span:5},r.a.createElement(T.a,{onChange:d("toDate"),defaultValue:c.toDate})),r.a.createElement(O.a,{span:6},r.a.createElement(C.a,{onChange:d("toTime"),defaultValue:c.toTime,format:"h:mm a",use12Hours:!0})))))),r.a.createElement(v.a,{gutter:6},r.a.createElement(O.a,{span:6},r.a.createElement(b.a.Item,{label:"Interval (min)"},r.a.createElement(w.a,{onChange:s("interval"),style:{width:"100%"},value:c.interval,placeholder:"5"}))),r.a.createElement(O.a,{span:13},r.a.createElement(b.a.Item,{label:"Location"},r.a.createElement(j.a,{onChange:function(e){m(D({},c,{location:e.currentTarget.value}))},value:c.location,placeholder:"Hamilton, New Zealand"}))),r.a.createElement(O.a,{span:5},r.a.createElement(b.a.Item,null,r.a.createElement(x.a,{type:"primary",disabled:a,onClick:i},a?"Calculating...":"Calculate"))))))},_=a(192),F=a(941),S=F.a.Text,P=function(e){var t=e.tempData,a=e.scheduleData;if(t.length>0){var n=a.slice(1).find((function(e){return!e.heating}))||a[0]||{heating:!1,time:t[0].time},l=t.filter((function(e){return e.time>n.time})).map((function(e){return e.temp})),o=Math.max.apply(Math,Object(_.a)(l)).toFixed(2),c=Math.min.apply(Math,Object(_.a)(l)).toFixed(2),m=(l.reduce((function(e,t){return e+t}))/l.length).toFixed(2),i=function(e){var t=Math.floor(e.length/2),a=Object(_.a)(e).sort((function(e,t){return e-t}));return e.length%2!==0?a[t]:(a[t-1]+a[t])/2}(l).toFixed(2),u=function(e){var t=0,a=void 0;return e.forEach((function(e){!e.heating&&a?(t+=e.time-a.time,a=void 0):e.heating&&(a=e)})),t}(a),s=d()().startOf("day").add(u,"seconds").format("H:mm:ss").split(":"),p="".concat(s[0],"h ").concat(s[1],"m"),E=(u*t[0].heater/36e5).toFixed(2),h={paddingTop:5,paddingBottom:5};return r.a.createElement("div",{style:{padding:15,textAlign:"left"}},r.a.createElement(v.a,{style:h},r.a.createElement(O.a,{span:12},r.a.createElement(S,{strong:!0},"Target:")),r.a.createElement(O.a,{span:12},r.a.createElement(S,null,t[0].target.toFixed(2)," \xb0C"))),r.a.createElement(v.a,{style:h},r.a.createElement(O.a,{span:12},r.a.createElement(S,{strong:!0},"Range:")),r.a.createElement(O.a,{span:12},r.a.createElement(S,null,c," \xb0C - ",o))),r.a.createElement(v.a,{style:h},r.a.createElement(O.a,{span:12},r.a.createElement(S,{strong:!0},"Mean:")),r.a.createElement(O.a,{span:12},r.a.createElement(S,null,m," \xb0C"))),r.a.createElement(v.a,{style:h},r.a.createElement(O.a,{span:12},r.a.createElement(S,{strong:!0},"Median:")),r.a.createElement(O.a,{span:12},r.a.createElement(S,null,i," \xb0C"))),r.a.createElement(v.a,{style:h},r.a.createElement(O.a,{span:12},r.a.createElement(S,{strong:!0},"Heating Time:")),r.a.createElement(O.a,{span:12},r.a.createElement(S,null,p))),r.a.createElement(v.a,{style:h},r.a.createElement(O.a,{span:12},r.a.createElement(S,{strong:!0},"Energy Usage:")),r.a.createElement(O.a,{span:12},r.a.createElement(S,null,E," kWh"))))}return r.a.createElement("div",{style:{marginTop:20}},r.a.createElement(S,{type:"secondary",strong:!0},"No data"))},A=a(945),L=a(262),Y=a(940),H=a(66),M=function(){var e=Object(n.useState)([]),t=Object(u.a)(e,2),a=t[0],l=t[1],o=Object(n.useState)([]),c=Object(u.a)(o,2),s=c[0],p=c[1],E=Object(n.useState)(!1),h=Object(u.a)(E,2),g=h[0],b=h[1],O=Object(n.useCallback)(function(){var e=Object(i.a)(m.a.mark((function e(t){var a,n;return m.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return b(!0),e.next=3,f.run_simulation(t);case 3:a=e.sent,b(!1),a&&(n=a.init_time,l(a.temp_hist.map((function(e,r){var l={temp:e,outdoor_temp:a.outdoor_temp_hist[r],heater:t.heater,target:t.target_temp,time:n};return n+=a.interval,l}))),p(a.control));case 6:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),[]);return r.a.createElement("div",{className:"App"},r.a.createElement(A.a,null,r.a.createElement(A.a.Content,{style:{padding:20,textAlign:"center"}},r.a.createElement(v.a,{style:{display:"inline-block"}},r.a.createElement(W,{onCalculate:O,disabled:g})),r.a.createElement(v.a,{style:{marginTop:20}},r.a.createElement("div",{style:{width:650,display:"inline-block"}},r.a.createElement(y.a,null,r.a.createElement(H.d,{width:600,height:400,data:a},r.a.createElement(H.c,{stroke:"#ab6832",dataKey:"target",name:"Target Temperature",unit:" \xb0C",dot:!1}),r.a.createElement(H.c,{stroke:"#7bb350",strokeWidth:2,dataKey:"temp",name:"Indoor Temperature",unit:" \xb0C",dot:!1}),r.a.createElement(H.c,{stroke:"#507bb3",strokeWidth:2,dataKey:"outdoor_temp",name:"Outdoor Temperature",unit:" \xb0C",dot:!1}),r.a.createElement(H.g,null,r.a.createElement(H.a,{value:"Temperature (\xb0C)",angle:-90})),r.a.createElement(H.f,{tickFormatter:function(e){return d.a.unix(e).format("LT")},dataKey:"time"}),r.a.createElement(H.e,{labelFormatter:function(e){return d.a.unix(parseInt(e.toString())).format("ddd LT")},formatter:function(e){return"number"===typeof e?Math.round(100*e)/100:e}}),r.a.createElement(H.b,null)))),r.a.createElement("div",{style:{marginLeft:20,width:250,display:"inline-block",verticalAlign:"top"}},r.a.createElement(y.a,{style:{height:450},bodyStyle:{padding:0,height:"100%"}},r.a.createElement(L.a,{defaultActiveKey:"1",style:{display:"block",height:"100%"}},r.a.createElement(L.a.TabPane,{tab:"Statistics",key:"1",style:{height:"100%",overflowY:"auto"}},r.a.createElement(P,{tempData:a,scheduleData:s})),r.a.createElement(L.a.TabPane,{tab:"Schedule",key:"2",style:{height:"100%",overflowY:"auto"}},s.length>0?r.a.createElement(Y.a,null,s.slice(1).map((function(e,t){return r.a.createElement(Y.a.Item,{key:t},r.a.createElement(F.a.Text,{strong:!0},e.heating?"On":"Off")," - ",d.a.unix(e.time).format("ddd LT"))}))):r.a.createElement("div",{style:{marginTop:20}},r.a.createElement(F.a.Text,{type:"secondary",strong:!0},"No data"))))))))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));o.a.render(r.a.createElement(M,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()}))}},[[447,1,2]]]);
//# sourceMappingURL=main.8571487e.chunk.js.map