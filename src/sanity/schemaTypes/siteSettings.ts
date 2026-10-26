export default {
  name: 'siteSettings',
  title: 'Site Settings',
  type: 'document',
  fields: [
    {
      name: 'brandName',
      title: 'Brand Name',
      type: 'string',
      initialValue: 'HOOX'
    },
    {
      name: 'tagline',
      title: 'Tagline',
      type: 'string',
      initialValue: 'Strategy & growth advisory'
    },
    {
      name: 'heroHeadline',
      title: 'Hero Headline',
      type: 'string',
      initialValue: 'We help growing companies decide what to stop doing.'
    },
    {
      name: 'heroSubhead',
      title: 'Hero Subhead',
      type: 'text',
      initialValue: 'Two partners, four clients at a time. We help you decide what matters, then stay until it works.'
    },
    {
      name: 'ctaNote',
      title: 'Call to Action Subtitle',
      type: 'string',
      initialValue: 'Thirty minutes with a partner. Free, and useful either way.'
    },
    {
      name: 'contactEmail',
      title: 'Contact Email',
      type: 'string',
      initialValue: 'hello@hoox.example'
    },
    {
      name: 'contactPhone',
      title: 'Contact Phone',
      type: 'string',
      initialValue: '+44 20 7946 0920'
    },
    {
      name: 'locations',
      title: 'Offices / Locations',
      type: 'string',
      initialValue: 'London / Lisbon / Remote'
    },
    {
      name: 'defaultPalette',
      title: 'Default Palette',
      type: 'string',
      options: {
        list: [
          { title: 'Cobalt', value: 'cobalt' },
          { title: 'Mint', value: 'mint' },
          { title: 'Lime', value: 'lime' },
          { title: 'Violet', value: 'violet' }
        ]
      },
      initialValue: 'cobalt'
    }
  ]
};
