{%load static%}
{%load i18n%}

/////SOCKETIO
recibePrinterConection: ((data) => {
    if(self.Sellpoint.printer == data.name){
        if (data.name != self.ActivePrinter.name){
            self.ActivePrinter = data
            PrivateSocket = io.connect(self.ActivePrinter.url, {resource: 'PrivateSocket/socket.io', 'force new connection': true});
            UnBlock()
        }
    }
}),
recibePrintTicket: ((data) => {
    //if(data.sellpoint.vendors.includes({{request.user.id}}))
    self.Tickets.unshift(data)
}),
recibeScanTicket: ((data) => {
    updateTicket = self.Tickets.find(function(ticket) {
        return ticket.key == data.key;
    });
    if (updateTicket){
        updateTicket.status = data.status
        updateTicket.barcode = data.barcode
        updateTicket.cut = data.cut
        self.LastTicketScan = data.barcode
    }
}),
recibeReloadSystem: ((data) => {
    self.reloadSystem()
}),
recibeGetStates: ((data) => {
    self.getStates()
}),