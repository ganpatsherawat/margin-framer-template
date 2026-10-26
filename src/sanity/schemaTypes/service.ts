export default {
  name: 'service',
  title: 'Service',
  type: 'document',
  fields: [
    {
      name: 'title',
      title: 'Title',
      type: 'string',
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'slug',
      title: 'Slug',
      type: 'slug',
      options: {
        source: 'title',
        maxLength: 96
      },
      validation: (Rule: any) => Rule.required()
    },
    {
      name: 'numberCode',
      title: 'Number Code (e.g. 01)',
      type: 'string'
    },
    {
      name: 'duration',
      title: 'Engagement Duration',
      type: 'string'
    },
    {
      name: 'priceFrom',
      title: 'Pricing Starting Point',
      type: 'string'
    },
    {
      name: 'summary',
      title: 'Short Summary',
      type: 'text',
      rows: 3
    },
    {
      name: 'deliverables',
      title: 'Key Deliverables',
      type: 'array',
      of: [{ type: 'string' }]
    },
    {
      name: 'idealFor',
      title: 'Ideal Company Stage / Fit',
      type: 'string'
    },
    {
      name: 'thumbnailImage',
      title: 'Hover Thumbnail Image',
      type: 'image',
      options: { hotspot: true }
    },
    {
      name: 'order',
      title: 'Display Order',
      type: 'number'
    }
  ]
};
