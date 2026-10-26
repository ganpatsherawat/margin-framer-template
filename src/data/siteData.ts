export interface ServiceItem {
  slug: string;
  numberCode: string;
  title: string;
  duration: string;
  priceFrom: string;
  summary: string;
  deliverables?: string[];
  thumbnailImage: string;
}

export interface CaseStudyItem {
  slug: string;
  title: string;
  industry: string;
  year: string;
  metricValue: string;
  metricLabel: string;
  headline: string;
  summary: string;
  coverImage: string;
  featured?: boolean;
}

export interface TestimonialItem {
  quote: string;
  author: string;
  initials: string;
  role: string;
  company: string;
  image: string;
}

export interface DecisionItem {
  text: string;
  status: 'not_now' | 'funded';
  tag?: string;
}

export const siteData = {
  brandName: 'HOOX',
  tagline: 'Strategy & growth advisory',
  metaDescription: 'A two-partner strategy and growth advisory for B2B companies between $5M and $50M in revenue. We find the few decisions that matter, make them with you, and stay until they are working.',
  consultationNote: 'Thirty minutes with a partner. Free.',
  availability: 'Booking from January 2027',
  contactEmail: 'hello@hoox.example',
  contactPhone: '+44 20 7946 0920',
  locations: 'London / Lisbon / Remote',
  
  hero: {
    headline: 'We help growing companies decide what to stop doing.',
    subhead: 'Two partners, four clients at a time. We help you decide what matters, then stay until it works.',
    ctaText: 'Book an intro call',
    heroImage: 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=2400&q=80',
    heroImageAlt: 'Four people walking along an elevated white path that forms a strategic trajectory.'
  },

  decisionRecord: {
    header: 'Decision record · Q1 2027',
    title: 'The not-now list',
    items: [
      { text: 'Enter the German market', status: 'not_now' },
      { text: 'Rebuild the ICP around retention', status: 'funded', tag: 'Fund' },
      { text: 'Rebrand before the Series B', status: 'not_now' },
      { text: 'Move pricing to annual contracts', status: 'funded', tag: 'Fund' },
      { text: 'Hire three more SDRs', status: 'not_now' }
    ] as DecisionItem[],
    stats: '3 not now · 2 funded',
    cardImage: 'https://images.unsplash.com/photo-1517245386807-bb43f82c33c4?auto=format&fit=crop&w=2400&q=80',
    cardImageAlt: 'A team collaborating around a table in a glass-walled conference room at night.'
  },

  clientMarquee: [
    'fernhill',
    'Oakmont Health',
    'quarry/labs',
    'TIDEwater',
    'HALWARD',
    'kestrel'
  ],

  services: [
    {
      slug: 'positioning',
      numberCode: '01',
      title: 'Positioning',
      duration: '6 weeks',
      priceFrom: 'From $24,000',
      summary: 'Sharpen your point of view, identify your ideal customer profile, and align every sales conversation around how you uniquely win.',
      deliverables: [
        'Customer interview insights and win/loss audit',
        'Competitive differentiation thesis',
        'Core messaging matrix and narrative script',
        'Sales battlecard and qualification rubric'
      ],
      thumbnailImage: 'https://images.unsplash.com/photo-1531403009284-440f080d1e12?auto=format&fit=crop&w=1200&q=80'
    },
    {
      slug: 'go-to-market',
      numberCode: '02',
      title: 'Go-to-market',
      duration: '8–10 weeks',
      priceFrom: 'From $38,000',
      summary: 'Rebuild your commercial engine. We align marketing demand, outbound focus, and customer success around retention and deal velocity.',
      deliverables: [
        'Commercial pipeline architecture',
        'Inbound and outbound playbooks',
        'Pricing packaging and contract transition roadmap',
        'RevOps dashboard and metric governance'
      ],
      thumbnailImage: 'https://images.unsplash.com/photo-1509316975850-ff9c5deb0cd9?auto=format&fit=crop&w=1200&q=80'
    },
    {
      slug: 'advisory',
      numberCode: '03',
      title: 'Advisory',
      duration: '6 months minimum',
      priceFrom: 'From $8,000 / mo',
      summary: 'An embedded strategic advisor directly with founders. We join leadership decisions, review major bets, and hold the line on focus.',
      deliverables: [
        'Weekly executive strategic sparring sessions',
        'Continuous decision governance and veto reviews',
        'Board deck preparation and narrative refinement',
        'Quarterly focus planning and stop-doing lists'
      ],
      thumbnailImage: 'https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=1200&q=80'
    }
  ] as ServiceItem[],

  featuredCase: {
    slug: 'fernhill',
    client: 'Fernhill',
    industry: 'Freight software',
    year: '2025',
    metricValue: '+41%',
    metricLabel: 'more qualified pipeline, two quarters after Fernhill stopped selling to everyone.',
    readText: 'Read the case'
  },

  caseStudies: [
    {
      slug: 'fernhill',
      title: 'Fernhill',
      industry: 'Freight software',
      year: '2025',
      metricValue: '+41%',
      metricLabel: 'Qualified pipeline',
      headline: 'Narrowing the ICP to expand revenue velocity',
      summary: 'How focusing exclusively on high-retention enterprise logistics operators transformed deal cycles from 9 months to 45 days.',
      coverImage: 'https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?auto=format&fit=crop&w=1200&q=80',
      featured: true
    },
    {
      slug: 'oakmont-health',
      title: 'Oakmont Health',
      industry: 'Clinic software',
      year: '2025',
      metricValue: '2.3×',
      metricLabel: 'Enterprise win rate',
      headline: 'From commodity tool to clinical workflow backbone',
      summary: 'Restructuring enterprise pricing and stopping custom feature requests to double win rates against legacy health conglomerates.',
      coverImage: 'https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=1200&q=80'
    },
    {
      slug: 'tidewater',
      title: 'Tidewater Studio',
      industry: 'Architecture',
      year: '2026',
      metricValue: '+33%',
      metricLabel: 'Average project fee',
      headline: 'Moving from RFP fee competition to premium retained masterplans',
      summary: 'Turning down speculative pitch requests to command top-tier advisory retainers across major urban development bids.',
      coverImage: 'https://images.unsplash.com/photo-1503387762-592deb58ef4e?auto=format&fit=crop&w=1200&q=80'
    }
  ] as CaseStudyItem[],

  testimonial: {
    quote: '“Nora talked us out of a rebrand. It was the most valuable thing anyone told us that year.”',
    author: 'Elena Sousa',
    initials: 'ES',
    role: 'Founder',
    company: 'Tidewater Studio',
    image: 'https://images.unsplash.com/photo-1513694203232-719a280e022f?auto=format&fit=crop&w=1200&q=80'
  } as TestimonialItem,

  ctaBanner: {
    badge: 'Booking from January 2027',
    headline: 'Tell us what’s stuck.',
    subhead: 'Thirty minutes with a partner. Free, and useful either way.',
    ctaButton: 'Book an intro call'
  },

  footer: {
    disclaimer: 'Client names, logos, figures, prices and testimonials on this site are samples. Replace them before launch.',
    copyright: '© 2026 HOOX Advisory. London / Lisbon / Remote.',
    styleGuide: './style-guide'
  }
};
