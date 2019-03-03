<template lang="pug">
  div
    .row.row-bordered.my-4
      .col-2
        a.card.card-hover.text-dark.my-2(href='javascript:void(0)')
          b-card-body.text-center.py-5
            .lnr.lnr-home.display-3.text-primary
            h5.m-0.mt-3 Getting starged
      .col-2
        a.card.card-hover.text-dark.my-2(href='javascript:void(0)')
          b-card-body.text-center.py-5
            .lnr.lnr-users.display-3.text-primary
            h5.m-0.mt-3 Accounts
      .col-2
        a.card.card-hover.text-dark.my-2(href='javascript:void(0)')
          b-card-body.text-center.py-5
            .lnr.lnr-apartment.display-3.text-primary
            h5.m-0.mt-3 Membership
      .col-2
        a.card.card-hover.text-dark.my-2(href='javascript:void(0)')
          b-card-body.text-center.py-5
            .lnr.lnr-lock.display-3.text-primary
            h5.m-0.mt-3 Privacy
      .col-2
        a.card.card-hover.text-dark.my-2(href='javascript:void(0)')
          b-card-body.text-center.py-5
            .lnr.lnr-bug.display-3.text-primary
            h5.m-0.mt-3 Issues
      .col-2
        a.card.card-hover.text-dark.my-2(href='javascript:void(0)')
          b-card-body.text-center.py-5
            .lnr.lnr-bubble.display-3.text-primary
            h5.m-0.mt-3 Contacts
</template>

<script>
export default {
  name: 'pages-help-center',
  metaInfo: {
    title: 'Help center - Pages'
  }
}
</script>
